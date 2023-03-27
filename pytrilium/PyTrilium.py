from .PyTriliumCustomClient import PyTriliumCustomClient

class PyTrilium(PyTriliumCustomClient):
    def __init__(self, url, token=None, password=None, debug=False) -> None:
        """Initializes the PyTrilium class. You need to either provide an ETAPI token OR a password (which will then be used to generate an ETAPI token).

        Parameters
        ----------
        url : str
            The URL of the Trilium instance. This should include the protocol (http:// or https://) and the port if it is not the protocol's respective port (443 for https, 80 for http). e.g. `https://trilium.example.com:8080`
        token : str, optional
            The token for the Trilium instance. This can be found in the Trilium settings.
        debug : bool, optional
            If you would like to enable debugging, set this to True, by default False
        password : str, optional
            The password for the Trilium instance. This can be found in the Trilium settings. This is only required if you are using Trilium's built-in authentication, by default None
        """
        super().__init__(url, token, debug)

        # Set up the requests session, the validate that either a password or a token was provided
        # If not, return an error
        self.make_requests_session()
        if not token and not password:
            raise ValueError("You must provide either a token or a password.")
        if password:
            self.token = self.auth_login(password)
        if token:
            self.token = token
        self.set_session_auth(self.token)

        # Attempt a basic call to make sure that the token is valid
        self.attempt_basic_call()

    def auth_login(self, password:str) -> str:
        """Authenticate to Trilium using a password. This should not be called manually. This will return the token that can be used to authenticate to Trilium in future requests.

        Parameters
        ----------
        password : str
            The password to send to Trilium

        Returns
        -------
        str
            The ETAPI token that can be used to authenticate to Trilium in future requests.
        """

        # Returns {"authToken": "33xHpBRHetAN_fh3g0B7MQaaaaj1871fbXLbbK4JAT06GGmZOSwet56M="}
        data = {"password": password}

        resp = self.make_request("/auth/login", data=data, method="POST")
        return resp.json()["authToken"]
    
    def auth_logout(self):
        """Logs out of Trilium. This should not be called manually."""
        self.make_request("/auth/logout", method="POST")

    def get_inbox_note(self, date:str):
        """Get the inbox's note for a date.

        Parameters
        ----------
        date : str
            The date which you would like to fetch the inbox note for. This should be in the format of YYYY-MM-DD. e.g. `2021-01-01`
        """
        self.make_request(f"/inbox/{date}")
    
    def print_custom_functions(self):

        dont_show_these_funcs = ["url", "token", "session"]

        list_of_funcs = dir(self)
        for func in list_of_funcs:
            if "__" not in func and "logger" not in func:
                if func not in dont_show_these_funcs:
                    print(func)