import requests


class JsonRequest:
    def __init__(self, url, jsonData):
        self.url = url
        self.jsonData = jsonData

    def submit(self):
        header = {'Content-Type': 'application/json'}
        response = requests.post(self.url, data=self.jsonData, headers=header)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        else:
            return response
