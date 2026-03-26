from dataclasses import dataclass
from datetime import date
from enum import Enum

class TransactionType(Enum):
    INCOME = "income"
    OUTCOME = "outcome"

@dataclass
class Transaction:
    transaction_date: date
    amount: int
    transaction_type: TransactionType
    memo: str

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("amount should be more than 0")
        if not isinstance(self.transaction_date, date):
            raise TypeError("date must be datetime.date")
        
    def to_dict(self):
        return {
            "date": self.transaction_date.isoformat(),
            "amount": self.amount,
            "type": self.transaction_type.value,
            "memo": self.memo
        }
