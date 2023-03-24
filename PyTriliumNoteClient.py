from PyTriliumClient import PyTriliumClient

class PyTriliumNoteClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)
    
    def get_note_by_id(self, note_id):
        return self.make_request(f"/notes/{note_id}")
