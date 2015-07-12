import requests


class JsonRequest:
    def __init__(self, url, jsonData, header):
        self.url = url
        self.jsonData = jsonData
        self.header = {'Content-Type': 'application/json'}
        self.header.update(header)

    def submit(self):
        response = requests.post(self.url, data=self.jsonData,
                                 headers=self.header)
        return response
