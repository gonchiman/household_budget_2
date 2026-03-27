import pytest

from src.transaction_repository import TransactionRepository
from src.paths import TRANSACTION_CSV_PATH


def test_transaction_repository_create_file():
    TransactionRepository()
    assert TRANSACTION_CSV_PATH.exists()
