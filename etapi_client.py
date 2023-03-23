import log

class PyTriliumClient():
    def __init__(self, url, token, debug=False) -> None:
        
        self.url = url
        self.token = token

        self.logger = log.get_logger(logger_name='PyTriliumClient', log_file_name='PyTriliumClient.log', debug=debug)
        pass

    def make_request(self, api_endpoint, method="GET", body="", params={}) -> None:
        
        
        pass

    def clean_url(self) -> None:
        if '/etapi' not in self.url:
            self.url = self.url + '/etapi'
        if 'http' not in self.url and 'https' not in self.url:
            self.url = 'http://' + self.url
        pass

    def get_config(self) -> None:
        pass



    def get_notes(self) -> None:
        pass

