import MundipaggSmartwallet.consts as consts
import MundipaggSmartwallet.Utils as Utils
from MundipaggSmartwallet.Submitable import Submitable, PrintableResponse, ErrorResponse

transactionURL = consts.Mundipagg['URLS']['Transaction']

class CreditFinancialMovement(PrintableResponse):
    def __init__(self, ItemReference=None, AccountKey=None,
                 FinancialMovementKey=None):
        self.ItemReference = ItemReference
        self.AccountKey = AccountKey
        self.FinancialMovementKey = FinancialMovementKey

    def cancel(self, smartWalletKey):
        financialMovementUrl = "%s%s" % (transactionURL, self.FinancialMovementKey)
        Req = Utils.JsonRequest(financialMovementUrl, {}, header={
            "SmartWalletKey": smartWalletKey
        })

        response = Req.submit()
        if response.status_code == 500:
            raise ErrorResponse(response.json())
        else:
            return response.json()

class Transaction(PrintableResponse):
    def __init__(self, CreditFinancialMovementCollection, RequestKey,
                 Errors=None):
        self.CreditFinancialMovementCollection = [CreditFinancialMovement(**fm) for fm in CreditFinancialMovementCollection]
        self.RequestKey = RequestKey
        self.Errors = Errors


class TransactionCreator(Submitable):
    def __init__(self, CreditItemCollection=None, Order=None, RequestKey=None):
        self.CreditItemCollection = CreditItemCollection
        self.Order = Order
        self.RequestKey = RequestKey

    def create(self, smartWalletKey):
        return super(TransactionCreator, self).create(transactionURL, Transaction, smartWalletKey)
