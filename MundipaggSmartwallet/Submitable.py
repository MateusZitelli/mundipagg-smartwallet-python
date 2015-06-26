import json
import requests
import Utils


class Submitable:
    def __init__():
        pass

    def toJSON(self, SmartWalletKey):
        selfData = {k: v for k, v in self.__dict__.items() if v}
        selfData['SmartWalletKey'] = SmartWalletKey
        jsonData = json.dumps(selfData)
        return jsonData

    def create(self, creationUrl, ResponseClass, smartWalletKey):
        jsonData = self.toJSON(smartWalletKey)
        Req = Utils.JsonRequest(creationUrl, jsonData)
        response = None
        try:
            response = Req.submit()
        except requests.exceptions.HTTPError:
            raise

        responseDict = json.loads(response.json())
        return ResponseClass(*responseDict)
