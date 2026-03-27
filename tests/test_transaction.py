from datetime import date
import pytest

from src.transaction import Transaction, TransactionType


def test_transaction_values():
    date_ = date.today()
    amount = 1000
    type_ = TransactionType.INCOME
    memo = "bonus"

    t = Transaction(date_, amount, type_, memo)

    expected = [
        date.today(),
        1000,
        TransactionType.INCOME,
        "bonus"
    ]

    assert [
        t.transaction_date,
        t.amount,
        t.transaction_type,
        t.memo
    ] == expected

def test_transaction_negative_amount():
    date_ = date.today()
    amount = -1000
    type_ = TransactionType.INCOME
    memo = "bonus"

    with pytest.raises(ValueError):
        Transaction(date_, amount, type_, memo)
