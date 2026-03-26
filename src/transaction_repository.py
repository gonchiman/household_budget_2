import csv
from paths import TRANSACTION_CSV_PATH
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from transaction import Transaction

class TransactionRepository:
    def add(self, transaction : "Transaction"):
        if not TRANSACTION_CSV_PATH.exists():
            self._init_path()

        with open(TRANSACTION_CSV_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            data = transaction.to_dict()
            writer.writerow([
                data["date"],
                data["amount"],
                data["type"],
                data["memo"]
            ])

    def _init_path(self):
        with open(TRANSACTION_CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date",
                "amount",
                "type",
                "memo"
            ])