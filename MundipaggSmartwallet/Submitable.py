import json
import inspect

import MundipaggSmartwallet.Utils


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

        try:
            success = responseJson.pop('Success')
        except KeyError:
            success = None

        errors = responseJson.pop('Errors')

        # If not succeed or in case of success is None check if there is
        # errors
        if success is not None and not success or len(errors) != 0:
            descriptions = []

            for err in errors:
                descriptions.append(err)

            raise ErrorResponse(descriptions)

        return responseJson

    def create(self, creationUrl, ResponseClass, smartWalletKey):
        jsonData = self.toJSON(smartWalletKey)

        Req = Utils.JsonRequest(creationUrl, jsonData, header={
            "SmartWalletKey": smartWalletKey
        })

        response = Req.submit()
        responseDict = self.handleResponse(response)
        responseClassArgs = inspect.getargspec(ResponseClass.__init__)[0]
        desiredValues = {k: v for k, v in responseDict.items() if k in responseClassArgs}
        return ResponseClass(**desiredValues)

class PrintableResponse:
    def __repr__(self):
        attrs = {k: v for k, v in self.__dict__.items() if v}
        return "%s(%s)" % (self.__class__.__name__, str(attrs))
