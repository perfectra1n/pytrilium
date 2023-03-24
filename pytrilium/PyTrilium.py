from .PyTriliumNoteClient import PyTriliumNoteClient
from .PyTriliumBranchClient import PyTriliumBranchClient
from .PyTriliumAttributeClient import PyTriliumAttributeClient


class PyTrilium(PyTriliumNoteClient, PyTriliumBranchClient, PyTriliumAttributeClient):
    def __init__(self, url, token, debug=False) -> None:
        """Initializes the PyTrilium class.

        Parameters
        ----------
        url : str
            The URL of the Trilium instance. This should include the protocol (http:// or https://) and the port if it is not the protocol's respective port (443 for https, 80 for http). e.g. `https://trilium.example.com:8080`
        token : str
            The token for the Trilium instance. This can be found in the Trilium settings.
        debug : bool, optional
            If you would like to enable debugging, set this to True, by default False
        """
        super().__init__(url, token, debug)

        # Set up the requests session, and make a generic call to Trilium to validate that it works
        self.make_requests_session()
        self.attempt_basic_call()
