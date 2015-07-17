import consts
from Submitable import Submitable, PrintableResponse


class Transaction(PrintableResponse):
    def __init__(self, CreditFinancialMovementCollection, RequestKey,
                 Errors=None):
        self.CreditFinancialMovementCollection = CreditFinancialMovementCollection
        self.RequestKey = RequestKey
        self.Errors = Errors


class TransactionCreator(Submitable):
    def __init__(self, CreditItemCollection=None, Order=None, RequestKey=None):
        self.CreditItemCollection = CreditItemCollection
        self.Order = Order
        self.RequestKey = RequestKey

    def create(self, smartWalletKey):
        transactionURL = consts.Mundipagg['URLS']['Transaction']
        return super(TransactionCreator, self).create(transactionURL, Transaction, smartWalletKey)
