import requests
from .PyTriliumClient import PyTriliumClient


class PyTriliumBranchClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)

    def get_branch_by_id(self, branch_id: str) -> dict:
        """Given the Branch's ID, this will return the Branch's information.

        Parameters
        ----------
        branch_id : str
            Trilium's ID for the Branch, this can be seen by clicking the 'i' on the branch, near the top.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/branches/{branch_id}").json()
    
    def post_branch(self, data: str) -> requests.Response:
        """This will create a new Branch.

        Parameters
        ----------
        data : str
            The data to send to the Trilium API. This should be in the format of a JSON string.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request("/branches", method="POST", data=data)
    
    def patch_branch_by_id(self, branch_id: str, data: str) -> requests.Response:
        """Given the Branch's ID, this will update the Branch's information.

        Parameters
        ----------
        branch_id : str
            Trilium's ID for the Branch, this can be seen by clicking the 'i' on the branch, near the top.
        data : str
            The data to send to the Trilium API. This should be in the format of a JSON string.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/branches/{branch_id}", method="PATCH", data=data)
    
    def delete_branch_by_id(self, branch_id: str) -> requests.Response:
        """Given the Branch's ID, this will delete the Branch.

        Parameters
        ----------
        branch_id : str
            Trilium's ID for the Branch, this can be seen by clicking the 'i' on the branch, near the top.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/branches/{branch_id}", method="DELETE")
    