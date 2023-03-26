import requests
from .PyTriliumClient import PyTriliumClient


class PyTriliumCalendarClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)

    def get_year_note(self, year: str) -> requests.Response:
        return self.make_request(f"calendar/years/{year}")

    def get_weeks_note(self, weeks: str) -> requests.Response:
        return self.make_request(f"calendar/weeks/{weeks}")
    
    def get_months_note(self, months: str) -> requests.Response:
        return self.make_request(f"calendar/months/{months}")
    
    def get_days_note(self, date: str) -> requests.Response:
        return self.make_request(f"calendar/days/{date}")