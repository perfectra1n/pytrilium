import requests
from PyTriliumClient import PyTriliumClient

class PyTriliumNoteClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)
    
    def get_note_by_id(self, note_id) -> requests.Response:
        return self.make_request(f"/notes/{note_id}")
    
    def get_note_content_by_title(self, note_title):
