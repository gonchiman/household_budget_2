from datetime import date

from src.transaction import Transaction, TransactionType
from src.transaction_repository import TransactionRepository
from src.transaction_service import TransactionService


class FakeRepository:
    def __init__(self):
        self.saved_transaction = None

    def add(self, transaction: Transaction):
        self.saved_transaction = transaction


def test_add_transaction():
    repo = FakeRepository()
    service = TransactionService(repo)

    date_ = date.today()
    amount = 1000
    type_ = TransactionType.INCOME
    memo = "bonus"

    service.add_transaction(
        date_,
        amount,
        type_,
        memo
    )

    assert repo.saved_transaction is not None
    assert repo.saved_transaction.transaction_date == date_
    assert repo.saved_transaction.amount == amount
    assert repo.saved_transaction.transaction_type == type_
    assert repo.saved_transaction.memo == memo