import consts
from Submitable import Submitable


class Transaction:
    def __init__(self, AccountKey, AccountReference, Acquirer, DbaName,
                 DocumentNumber, DocumentType, Errors, LegalName, RequestKey):
        self.AccountReference = AccountReference
        self.LegalName = LegalName
        self.DbaName = DbaName
        self.DocumentNumber = DocumentNumber
        self.DocumentType = DocumentType
        self.RequestKey = RequestKey


class TransactionCreator(Submitable):
    def __init__(self, CreditItemCollection=None, Order=None, RequestKey=None):
        self.CreditItemCollection = CreditItemCollection
        self.Order = Order
        self.RequestKey = RequestKey

    def create(self, smartWalletKey):
        transactionURL = consts.Mundipagg['URLS']['Transaction']
        return super(TransactionCreator, self).create(transactionURL, Transaction)
