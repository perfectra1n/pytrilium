import requests
from .PyTriliumClient import PyTriliumClient

class PyTriliumNoteClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)
    
    def get_note_by_id(self, note_id: str) -> dict:
        """Given the Note's ID, this will return the Note's information.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/notes/{note_id}").json()
    
    def get_note_content_by_id(self, note_id: str) -> requests.Response:
        return self.make_request(f"/notes/{note_id}/content")
    
    def patch_note_by_id(self, note_id: str, data: str) -> requests.Response:
        return self.make_request(f"/notes/{note_id}", method="PATCH", data=data)
    
    def delete_note_by_id(self, note_id: str) -> requests.Response:
        return self.make_request(f"/notes/{note_id}", method="DELETE")