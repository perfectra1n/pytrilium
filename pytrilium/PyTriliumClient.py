import requests
from requests.adapters import HTTPAdapter, Retry

# Local import
from . import log


class PyTriliumClient:
    def __init__(self, url: str, token: str, debug: bool = False) -> None:
        """Initializes the PyTriliumClient class.

        Parameters
        ----------
        url : str
            The URL of the Trilium instance. This should include the protocol (http:// or https://) and the port if it is not the protocol's respective port (443 for https, 80 for http). e.g. `https://trilium.example.com:8080`
        token : str
            The token for the Trilium instance. This can be found in the Trilium settings.
        debug : bool, optional
            If you would like to enable debugging, set this to True, by default False

        Raises
        ------
        ValueError
            If the URL is invalid, this will raise a ValueError.
        """

        self.token = token
        if not self.clean_url(url):
            raise ValueError(
                "Invalid URL, please make sure to include https:// or http:// and that the URL is correct. The attempted URL was: "
                + self.url
            )

        self.logger = log.get_logger(
            logger_name="PyTriliumClient",
            log_file_name="PyTriliumClient.log",
            debug=debug,
            create_log_file=True,
        )

        # The valid response codes that can come from Triliu
        # everything else will be logged as a console warning
        self.valid_response_codes = [200, 201, 202, 204]

    def make_requests_session(self) -> None:
        """Creates a requests session with the token and user agent header."""
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "PyTriliumClient/0.0.1"})
        self.session.headers.update({"Authorization": self.token})

        # Set up retry logic
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])

        # Have it work for both http and https
        self.session.mount("https://", HTTPAdapter(max_retries=retries))
        self.session.mount("http://", HTTPAdapter(max_retries=retries))

    def make_request(self, api_endpoint: str, method="GET", data="", params={}) -> requests.Response:
        """Standard request method for making requests to the Trilium API.

        Parameters
        ----------
        api_endpoint : str
            The API endpoint to make the request to. This should not include the URL or the /etapi prefix.
        method : str, optional
            The HTTP method to use, by default "GET"
        data : str, optional
            The body data to send with the request, by default ""
        params : dict, optional
            The parameters to include in the API call, by default {}

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        # We use our own session that holds the token, so we shouldn't
        # need to enforce it here.

        request_url = self.url + api_endpoint
        req_resp = self.session.request(method, request_url, data=data, params=params)
        if req_resp.status_code not in self.valid_response_codes:
            self.logger.warning(
                f"Possible invalid response code: {str(req_resp.status_code)}, response text: {req_resp.text}"
            )
        return req_resp

    def clean_url(self, url: str) -> bool:
        """Cleans the URL to make sure it is valid.


        Parameters
        ----------
        url : str
            The URL to clean.

        Returns
        -------
        bool
            If the URL is valid, this will return True. If the URL is invalid, this will return False.
        """
        if "/etapi" not in url:
            url = url + "/etapi"
        if "http" not in url and "https" not in url:
            # Then this URL is just scuffed
            return False
        self.url = url

        return True

    def attempt_basic_call(self) -> None:
        """Attempts a basic call to the Trilium API to make sure that the URL and token are valid."""
        resp = self.make_request("/app-info")
        if resp.status_code not in self.valid_response_codes:
            raise ValueError(
                f"Invalid response code: {str(resp.status_code)}, response text: {resp.text}. Response code should be one of {self.valid_response_codes}. Please check your Trilium, URL, and token."
            )
