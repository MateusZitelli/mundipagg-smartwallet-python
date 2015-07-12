import json
import requests
import Utils
import xml.etree.ElementTree as etree

DataContract = "{http://schemas.datacontract.org/2004/07/SmartWalletService.DataContract}"

NODES = {
    "success": DataContract + 'Success',
    "ErrorItem": DataContract + 'ErrorItem',
    "Description": DataContract + 'Description',
}


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
        try:
            xmlTree = etree.fromstring(response.content)
        except etree.ParseError:
            raise

        if response.status_code != requests.codes.ok:
            descriptions = []
            errorItemPath = './/' + NODES["ErrorItem"]

            for el in xmlTree.findall(errorItemPath):
                descriptionNode = el.find(NODES["Description"])
                descriptions.append(descriptionNode.text)

            raise ErrorResponse(descriptions)

        responseDict = json.loads(response.json())
        return responseDict

    def create(self, creationUrl, ResponseClass, smartWalletKey):
        jsonData = self.toJSON(smartWalletKey)

        Req = Utils.JsonRequest(creationUrl, jsonData, header={
            "SmarWalletKey": smartWalletKey
        })

        response = Req.submit()
        resposeDict = self.handleResponse(response)
        return ResponseClass(*responseDict)
