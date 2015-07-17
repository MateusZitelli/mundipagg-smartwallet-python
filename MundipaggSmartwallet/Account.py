import consts
from Submitable import Submitable, PrintableResponse


class Account(PrintableResponse):
    def __init__(self, AccountKey=None, AccountReference=None, Acquirer=None, DbaName=None,
                 DocumentNumber=None, DocumentType=None, Errors=None, LegalName=None, RequestKey=None):
        self.AccountKey = AccountKey
        self.AccountReference = AccountReference
        self.Acquirer=Acquirer
        self.LegalName = LegalName
        self.DbaName = DbaName
        self.DocumentNumber = DocumentNumber
        self.DocumentType = DocumentType
        self.RequestKey = RequestKey


class AccountCreator(Submitable):
    def __init__(self, AccountReference=None, LegalName=None, DbaName=None,
                 DocumentNumber=None, DocumentType=None, Email=None,
                 PhoneNumber=None, Addresses=None, FinancialDetails=None,
                 RequestKey=None, MCC=None):
        self.AccountReference = AccountReference
        self.LegalName = LegalName
        self.DbaName = DbaName
        self.DocumentNumber = DocumentNumber
        self.DocumentType = DocumentType
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Addresses = Addresses
        self.FinancialDetails = FinancialDetails
        self.MCC = MCC
        self.RequestKey = RequestKey

    def create(self, smartWalletKey):
        accountURL = consts.Mundipagg['URLS']['Account']
        return super(AccountCreator, self).create(accountURL, Account, smartWalletKey)

