from .PyTriliumNoteClient import PyTriliumNoteClient
from .PyTriliumBranchClient import PyTriliumBranchClient
from .PyTriliumAttributeClient import PyTriliumAttributeClient
from .PyTriliumCalendarClient import PyTriliumCalendarClient
from .PyTriliumAttachmentClient import PyTriliumAttachmentClient


# This class inherits from everything else, but also implements custom functions
# so I'm creating this to help save my sanity in the future
class PyTriliumCustomClient(
    PyTriliumNoteClient, PyTriliumBranchClient, PyTriliumAttributeClient, PyTriliumCalendarClient, PyTriliumAttachmentClient
):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)
