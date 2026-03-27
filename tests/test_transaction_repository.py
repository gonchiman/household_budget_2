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

