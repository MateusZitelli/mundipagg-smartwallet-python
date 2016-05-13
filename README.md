# mundipagg-smartwallet-python
> Smartwallet Connector

# Important infomation
This connector was tested in October, 2015. However, to work with the SmartWallet I had to use the
staging version of the Mundipagg API. Therefore if you want to use a different version of the API
change the BASE_URL in the file consts.py.

# Usage examples

## Smart wallet account registration

```python
accountCreator = SWAccount.AccountCreator(
    AccountReference="String",
    LegalName="String",
    DbaName="String",
    DocumentNumber="String",
    DocumentType="String",
    Email="String",
    Addresses=[{
        "State": "String",
        "Country": "Brasil",
        "City": "String"
    }],
    FinancialDetails=[{
        "Bank": {
            "AccountNumber": "String",
            "AgencyNumber": "String",
            "BankCode": "String"
        }
    }])

account = accountCreator.create(settings.MERCHANT_KEY)
```

## Creating a new transaction

```python
 t = SWTransaction.TransactionCreator(CreditItemCollection=[
    {
        "AccountKey": account.key,
        "Description": "GenericItem",
        "FeeType": "Percent",
        "FeeValue": 10,
        "HoldTransaction": False,
        "SplitTransaction": True
    }])
transaction = t.create(settings.MERCHANT_KEY)
```

For fields specs check out the [MundiPagg docs](http://docs.mundipagg.com/v1.0/docs).
