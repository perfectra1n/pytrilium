import requests
from .PyTriliumClient import PyTriliumClient


class PyTriliumCalendarClient(PyTriliumClient):
    def __init__(self, url, token, debug=False) -> None:
        super().__init__(url, token, debug)

    def get_year_note(self, year: str) -> dict:
        """Get the note for a year, in Trilium's calendar.

        Parameters
        ----------
        year : str
            The year you want to fetch from Trilium's calendar.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"calendar/years/{year}").json()

    def get_weeks_note(self, weeks: str) -> dict:
        """Get the note for a week, in Trilium's calendar.

        Parameters
        ----------
        weeks : str
            The week you want to fetch from Trilium's calendar.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"calendar/weeks/{weeks}").json()
    
    def get_months_note(self, months: str) -> dict:
        """Get the note for a month, in Trilium's calendar.

        Parameters
        ----------
        months : str
            The month you want to fetch from Trilium's calendar.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"calendar/months/{months}").json()
    
    def get_days_note(self, date: str) -> dict:
        """Get the note for a day, in Trilium's calendar.

        Parameters
        ----------
        date : str
            The date you want to fetch from Trilium's calendar.

        Returns
        -------
        dict
            The JSON response from Trilium, as a dictionary.
        """
        return self.make_request(f"calendar/days/{date}").json()