import json
import pytest
from bank_analyzer import generate_report

@pytest.fixture
def transactions():
    return [
        {"account_id": "ACC001", "amount": 2000.0, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC002", "amount": 4000.0, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC003", "amount": 100000.0, "type": "deposit",  "date": "2021-04-01"}
    ]

@pytest.fixture
def sample_json(transactions, tmp_path):
    generate_report(transactions, tmp_path / "report.json")
    with open(tmp_path / "report.json", "r", encoding="utf-8") as f:
        sample_json = json.load(f)

    return sample_json

def test_correct_json(sample_json):
    assert sample_json is not None

def test_fields_on_json(sample_json):
    assert "total_deposits" in sample_json.keys()
    assert "total_withdrawals" in sample_json.keys()
    assert "net_flow" in sample_json.keys()
    assert "top_transaction" in sample_json.keys()
    assert "transactions_count" in sample_json.keys()


def test_correct_values_type_json(sample_json):
    assert isinstance(sample_json['total_deposits'], float)
    assert isinstance(sample_json['total_withdrawals'], float)
    assert isinstance(sample_json['net_flow'], float)
    assert isinstance(sample_json['top_transaction'], list)
    assert isinstance(sample_json['transactions_count'], int)
    assert isinstance(sample_json['top_transaction'][0]['amount'], float)
    assert isinstance(sample_json['top_transaction'][0]['date'], str)
    assert isinstance(sample_json['top_transaction'][0]['type'], str)
    assert isinstance(sample_json['top_transaction'][0]['account_id'], str)

def test_correct_values_json(sample_json):
    assert sample_json['net_flow'] is not None
    assert sample_json['net_flow'] == (sample_json['total_deposits'] - sample_json['total_withdrawals'])
    assert sample_json['top_transaction'] is not None
    assert sample_json['transactions_count'] >= 0
    assert sample_json['total_deposits'] >= 0
    assert sample_json['total_withdrawals'] >= 0
    assert sample_json['top_transaction'][0]['amount'] >= 0

