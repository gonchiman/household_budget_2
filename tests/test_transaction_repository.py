import csv
from datetime import date

from src.transaction import Transaction, TransactionType
from src.transaction_repository import TransactionRepository
from src.paths import TRANSACTION_CSV_PATH


def test_create_csv_file():
    TRANSACTION_CSV_PATH.unlink(missing_ok=True)

    TransactionRepository()

    assert TRANSACTION_CSV_PATH.exists()

def test_add_row():
    TRANSACTION_CSV_PATH.unlink(missing_ok=True)

    date_ = date.today()
    amount = 1000
    type_ = TransactionType.INCOME
    memo = "bonus"
    t = Transaction(date_, amount, type_, memo)

    tr = TransactionRepository()
    tr.add(t)
    expected = {
        "date": date_.isoformat(),
        "amount": str(amount),
        "type": type_.value,
        "memo": memo
    }

    with open(TRANSACTION_CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        assert rows[0] == expected

def test_get_all():
    TRANSACTION_CSV_PATH.unlink(missing_ok=True)

    date1 = date.today()
    amount1 = 1000
    type1 = TransactionType.INCOME
    memo1 = "bonus"
    t1 = Transaction(date1, amount1, type1, memo1)

    date2 = date.today()
    amount2 = 1000
    type2 = TransactionType.INCOME
    memo2 = "bonus"
    t2 = Transaction(date2, amount2, type2, memo2)

    tr = TransactionRepository()
    tr.add(t1)
    tr.add(t2)
    transactions = tr.get_all()

    assert len(transactions) == 2

    t = transactions[0]

    assert t.transaction_date == date1
    assert t.amount == amount1
    assert t.transaction_type == type1
    assert t.memo == memo1

    t = transactions[1]

    assert t.transaction_date == date2
    assert t.amount == amount2
    assert t.transaction_type == type2
    assert t.memo == memo2
