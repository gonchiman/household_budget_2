from src.transaction import Transaction, TransactionType
from datetime import date

def transaction_normal_test():
    date_ = date.today()
    amount = 1000
    type_ = TransactionType.INCOME
    memo = "bonus"

    t = Transaction(date_, amount, type_, memo)

    expected = {
        "date": date_.isoformat(),
        "amount": 1000,
        "type": TransactionType.INCOME.value,
        "memo": "bonus"
    }

    assert t.to_dict() == expected

def transaction_negative_amount_test():
    date_ = date.today()
    amount = -1000
    type_ = TransactionType.INCOME
    memo = "bonus"

    t = Transaction(date_, amount, type_, memo)

transaction_negative_amount_test()