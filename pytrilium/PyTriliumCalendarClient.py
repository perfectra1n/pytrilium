import requests
from .PyTriliumClient import PyTriliumClient


class PyTriliumCalendarClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)

    def get_year_note(self, year: str):
        self.make_request(f"calendar/years/{year}")
