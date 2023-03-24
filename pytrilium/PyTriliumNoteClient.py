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

    def get_note_content_by_id(self, note_id: str) -> str:
        """Given the Note's ID, this will return the Note's content.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.

        Returns
        -------
        str
            The content of the note, most likely in HTML format.
        """
        return self.make_request(f"/notes/{note_id}/content").text
    
    def put_note_content_by_id(self, note_id: str, data: str) -> requests.Response:
        """Given the Note's ID, this will update the Note's content.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.
        data : str
            The data to send to the Trilium API. This should be in the format of a JSON string.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/notes/{note_id}/content", method="PUT", data=data)

    def patch_note_by_id(self, note_id: str, data: str) -> requests.Response:
        """Given the Note's ID, this will update the Note's content.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.
        data : str
            The data to send to the Trilium API. This should be in the format of a JSON string.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/notes/{note_id}", method="PATCH", data=data)

    def delete_note_by_id(self, note_id: str) -> requests.Response:
        """Given the Note's ID, this will delete the Note.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """
        return self.make_request(f"/notes/{note_id}", method="DELETE")

    def export_note_by_id(self, note_id: str, filepath_to_save_export_zip: str, format="html") -> bool:
        """Given the Note's ID, export itself and all child notes into a singular .zip archive.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.
        filepath_to_save_export_zip : str
            The path of where to save the .zip archive that is generated by Trilium.
        format : str, optional
            The format to export the Notes in, by default "html". Can also be "markdown".

        Returns
        -------
        bool
            Returns True if the Note was exported successfully, and written to the path. Otherwise, returns False.
        """

        # If the filepath ends with a slash, this means that a directory was specified.
        # We should add the filename to the end of it.
        if filepath_to_save_export_zip.endswith("/"):
            filepath_to_save_export_zip += f"pytrilium_export_{note_id}.zip"

        # Make sure the filepath ends with .zip. If not, add it.
        if not filepath_to_save_export_zip.endswith(".zip"):
            filepath_to_save_export_zip += ".zip"

        try:
            params = {"format": format}
            response = self.make_request(f"/notes/{note_id}/export", params=params)

            with open(filepath_to_save_export_zip, "wb") as f:
                f.write(response.content)
        except Exception as e:
            print(e)
            return False
        return True

    def create_note_revision(self, note_id: str, data: str, format: str = "html") -> requests.Response:
        """Given the Note's ID, create a new revision of the Note.

        Parameters
        ----------
        note_id : str
            Trilium's ID for the Note, this can be seen by clicking the 'i' on the note, near the top.
        data : str
            The data to send to the Trilium API. This should be in the format of a JSON string.
        format : str, optional
            The format of which the data being provided is in. By default "html". Can also be "markdown".

        Returns
        -------
        requests.Response
            The response from the Trilium API.
        """

        params = {"format": format}
        return self.make_request(f"/notes/{note_id}/note-revision", method="POST", data=data, params=params)
