import csv
from datetime import date

from src.paths import TRANSACTION_CSV_PATH
from src.transaction import Transaction, TransactionType
from src.transaction_repository import TransactionRepository
from src.transaction_service import TransactionService


def test_add_transaction():
    TRANSACTION_CSV_PATH.unlink(missing_ok=True)

    date_ = date.today()
    amount = 1000
    type_ = TransactionType.INCOME
    memo = "bonus"

    tr = TransactionRepository()
    ts = TransactionService(tr)
    ts.add_transaction(
        date_,
        amount,
        type_,
        memo
    )

    expected = {
        "date": date_.isoformat(),
        "amount": str(amount),
        "type": type_.value,
        "memo": memo
    }

    with open(TRANSACTION_CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        assert len(rows) == 1
        assert rows[0] == expected