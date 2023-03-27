import requests
from .PyTriliumClient import PyTriliumClient


class PyTriliumAttributeClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)

    def get_attribute_by_id(self, attribute_id: str) -> dict:
        """Given the Attribute's ID, this will return the Attribute's information.

        Parameters
        ----------
        attribute_id : str
            Trilium's ID for the Attribute, this can be seen by clicking the 'i' on the attribute, near the top.

        Returns
        -------
        dict
            The response from the Trilium API.
        """
        return self.make_request(f"/attributes/{attribute_id}").json()

    def post_attribute(self, data: str) -> dict:
        """This will create a new Attribute.

        Parameters
        ----------
        data : str
            The data to send to the Trilium API.This should be in the format of a string.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request("/attributes", method="POST", data=data).json()
