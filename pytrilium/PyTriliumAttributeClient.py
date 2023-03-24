from .PyTriliumClient import PyTriliumClient


class PyTriliumAttributeClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)
