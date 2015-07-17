import json
import requests
import Utils


class ErrorResponse(BaseException):
    def __init__(self, descriptions):
        self.descriptions = descriptions


class Submitable:
    def __init__():
        pass

    def toJSON(self, smartWalletKey):
        selfData = {k: v for k, v in self.__dict__.items() if v}
        selfData['SmartWalletKey'] = smartWalletKey
        jsonData = json.dumps(selfData)
        return jsonData

    def handleResponse(self, response):
        responseJson = response.json()

        if response.status_code != requests.codes.ok:
            descriptions = []

            for err in responseJson['Errors']:
                descriptions.append(err)

            raise ErrorResponse(descriptions)

        responseDict = json.loads(response.json())
        return responseDict

    def create(self, creationUrl, ResponseClass, smartWalletKey):
        jsonData = self.toJSON(smartWalletKey)
        print(jsonData)

        Req = Utils.JsonRequest(creationUrl, jsonData, header={
            "SmartWalletKey": smartWalletKey
        })

        response = Req.submit()
        resposeDict = self.handleResponse(response)
        return ResponseClass(*resposeDict)
