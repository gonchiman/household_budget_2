from src.transaction import Transaction, TransactionType
from src.transaction_repository import TransactionRepository
from src.paths import TRANSACTION_CSV_PATH
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

    try:
        t = Transaction(date_, amount, type_, memo)
        assert False, "this test should be error"
    except (AssertionError, ValueError):
        pass

def transaction_repository_create_file_test():
    tr = TransactionRepository()
    assert TRANSACTION_CSV_PATH.exists()

### test ###

transaction_negative_amount_test()