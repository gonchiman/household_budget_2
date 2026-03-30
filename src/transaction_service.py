from datetime import date

from src.transaction import Transaction, TransactionType
from src.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self._repository = repository

    def add_transaction(
        self,
        transaction_date: date,
        amount: int,
        transaction_type: TransactionType,
        memo: str
    ) -> None:
        transaction = Transaction(
            transaction_date=transaction_date,
            amount=amount,
            transaction_type=transaction_type,
            memo=memo
        )
        self._repository.add(transaction)

    def get_all_transactions(self) -> list[Transaction]:
        return self._repository.get_all()