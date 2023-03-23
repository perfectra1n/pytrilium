import requests
from requests.adapters import HTTPAdapter, Retry

# Local import
import log


class PyTriliumClient:
    def __init__(self, url, token, debug=False) -> None:
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

        self.valid_response_codes = [200, 201, 202, 204]
        self.make_requests_session()
        self.attempt_basic_call()

    def make_requests_session(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "PyTriliumClient/0.0.1"})
        self.session.headers.update({"Authorization": self.token})

        # Set up retry logic
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])

        # Have it work for both http and https
        self.session.mount("https://", HTTPAdapter(max_retries=retries))
        self.session.mount("http://", HTTPAdapter(max_retries=retries))

    def make_request(self, api_endpoint, method="GET", data="", params={}) -> None:
        # We use our own session that holds the token, so we shouldn't
        # need to enforce it here.

        request_url = self.url + api_endpoint
        req_resp = self.session.request(method, request_url, data=data, params=params)
        if req_resp.status_code not in self.valid_response_codes:
            self.logger.warning(
                f"Possible invalid response code: {str(req_resp.status_code)}, response text: {req_resp.text}"
            )
        return req_resp

    def clean_url(self, url) -> None:
        if "/etapi" not in url:
            url = url + "/etapi"
        if "http" not in url and "https" not in url:
            # Then this URL is just scuffed
            return False
        self.url = url

        return True

    def attempt_basic_call(self) -> None:
        resp = self.make_request("/app-info")
        if resp.status_code not in self.valid_response_codes:
            raise ValueError(
                f"Invalid response code: {str(resp.status_code)}, response text: {resp.text}. Response code should be one of {self.valid_response_codes}. Please check your Trilium, URL, and token."
            )

        self.logger.info(resp.json())
        pass

    def get_config(self) -> None:
        pass

    def get_notes(self) -> None:
        pass
