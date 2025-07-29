import requests
from .PyTriliumClient import PyTriliumClient


class PyTriliumAttachmentClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)

    def create_attachment(self, data: str) -> dict:
        """Create a new attachment.

        Parameters
        ----------
        data : str
            The data to send to the Trilium API. This should be in the format of a string.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request("/attachments", method="POST", data=data).json()

    def get_attachment_by_id(self, attachment_id: str) -> dict:
        """Given the Attachment's ID, this will return the Attachment's metadata.

        Parameters
        ----------
        attachment_id : str
            Trilium's ID for the Attachment.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"/attachments/{attachment_id}").json()

    def patch_attachment_by_id(self, attachment_id: str, data: str) -> dict:
        """Given the Attachment's ID, this will update the Attachment's metadata.

        Parameters
        ----------
        attachment_id : str
            Trilium's ID for the Attachment.
        data : str
            The data to send to the Trilium API. This should be in the format of a string.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"/attachments/{attachment_id}", method="PATCH", data=data).json()

    def delete_attachment_by_id(self, attachment_id: str) -> dict:
        """Given the Attachment's ID, this will delete the Attachment.

        Parameters
        ----------
        attachment_id : str
            Trilium's ID for the Attachment.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"/attachments/{attachment_id}", method="DELETE").json()

    def get_attachment_content_by_id(self, attachment_id: str) -> bytes:
        """Given the Attachment's ID, this will return the Attachment's content.

        Parameters
        ----------
        attachment_id : str
            Trilium's ID for the Attachment.

        Returns
        -------
        bytes
            The content of the attachment as bytes.
        """
        return self.make_request(f"/attachments/{attachment_id}/content").content

    def put_attachment_content_by_id(self, attachment_id: str, data: bytes) -> dict:
        """Given the Attachment's ID, this will update the Attachment's content.

        Parameters
        ----------
        attachment_id : str
            Trilium's ID for the Attachment.
        data : bytes
            The binary data to send to the Trilium API.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"/attachments/{attachment_id}/content", method="PUT", data=data).json()