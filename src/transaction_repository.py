import csv
from paths import TRANSACTION_CSV_PATH
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from transaction import Transaction

class TransactionRepository:
    COLUMNS = ["date", "amount", "type", "memo"]

    def __init__(self):
        if not TRANSACTION_CSV_PATH.exists():
            self._create_file_with_header()

    def add(self, transaction : "Transaction") -> None:
        with open(TRANSACTION_CSV_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self._transaction_to_csv_row(transaction))

    def _create_file_with_header(self) -> None:
        with open(TRANSACTION_CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.COLUMNS)

    def _transaction_to_csv_row(self, transaction: "Transaction") -> list:
        return [
            transaction.transaction_date.isoformat(),
            transaction.amount,
            transaction.transaction_type.value,
            transaction.memo
        ]
