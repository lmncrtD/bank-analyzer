import pytest
import csv
from bank_analyzer import get_total_by_type
from bank_analyzer import get_transactions_by_account
from bank_analyzer import get_top_transaction

@pytest.fixture
def sample_csv():
    return [
        {"account_id": "ACC001", "amount": 2000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC003", "amount": 3000.00, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 4000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC004", "amount": 100000.00, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 100000.00, "type": "deposit", "date": "2021-04-01"}
    ]


def test_correct_total_by_type(sample_csv):
    assert get_total_by_type(sample_csv, "deposit") >= 0.0
    assert get_total_by_type(sample_csv, "withdrawal") >= 0.0
    assert isinstance(get_total_by_type(sample_csv, "deposit"), float)
    assert isinstance(get_total_by_type(sample_csv, "withdrawal"), float)
    assert get_total_by_type([], "deposit") == 0.0
    assert get_total_by_type([], "withdrawal") == 0.0

def test_correct_transactions_by_account(sample_csv):
    assert "ACC001" in [x['account_id'] for x in get_transactions_by_account(sample_csv, "ACC001")]
    assert get_transactions_by_account(sample_csv, "ACC001") == [
        {"account_id": "ACC001", "amount": 2000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 4000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 100000.00, "type": "deposit", "date": "2021-04-01"}
    ]
    assert "ACC003" not in get_transactions_by_account(sample_csv, "ACC001")
    assert len(get_transactions_by_account(sample_csv, "ACC001")) == 3

def test_top_transactions(sample_csv):
    assert get_top_transaction(sample_csv) == [
        {"account_id": "ACC004", "amount": 100000.00, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 100000.00, "type": "deposit", "date": "2021-04-01"}
    ]