import pytest
import json
from bank_analyzer import TransactionAnalyzer

@pytest.fixture
def sample_csv():
    return [
        {"account_id": "ACC001", "amount": 2000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC003", "amount": 3000.00, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 4000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC004", "amount": 100000.00, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 100000.00, "type": "deposit", "date": "2021-04-01"}
    ]

@pytest.fixture
def transactions():
    return [
        {"account_id": "ACC001", "amount": 2000.0, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC002", "amount": 4000.0, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC003", "amount": 100000.0, "type": "deposit",  "date": "2021-04-01"}
    ]

@pytest.fixture
def sample_json(transactions, tmp_path):
    report = TransactionAnalyzer(transactions)
    report.generate_report(tmp_path / "report.json")
    with open(tmp_path / "report.json", "r", encoding="utf-8") as f:
        sample_json = json.load(f)

    return sample_json


def test_correct_total_by_type(sample_csv):
    transactions = TransactionAnalyzer(sample_csv)
    assert transactions.get_total_by_type("deposit") >= 0.0
    assert transactions.get_total_by_type("withdrawal") >= 0.0
    assert isinstance(transactions.get_total_by_type("deposit"), float)
    assert isinstance(transactions.get_total_by_type("withdrawal"), float)
    assert TransactionAnalyzer([]).get_total_by_type("deposit") == 0.0
    assert TransactionAnalyzer([]).get_total_by_type("withdrawal") == 0.0

def test_correct_transactions_by_account(sample_csv):
    transactions = TransactionAnalyzer(sample_csv)
    assert "ACC001" in [x['account_id'] for x in transactions.get_transactions_by_account("ACC001")]
    assert transactions.get_transactions_by_account("ACC001") == [
        {"account_id": "ACC001", "amount": 2000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 4000.00, "type": "deposit", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 100000.00, "type": "deposit", "date": "2021-04-01"}
    ]
    assert "ACC003" not in transactions.get_transactions_by_account("ACC001")
    assert len(transactions.get_transactions_by_account("ACC001")) == 3

def test_top_transactions(sample_csv):
    transactions = TransactionAnalyzer(sample_csv)
    assert transactions.get_top_transaction() == [
        {"account_id": "ACC004", "amount": 100000.00, "type": "withdrawal", "date": "2021-04-01"},
        {"account_id": "ACC001", "amount": 100000.00, "type": "deposit", "date": "2021-04-01"}
    ]

def test_summary(sample_csv):
    transactions = TransactionAnalyzer(sample_csv)
    assert "total_deposits" in transactions.summary().keys()
    assert "total_withdrawals" in transactions.summary().keys()
    assert "net_flow" in transactions.summary().keys()
    assert "top_transaction" in transactions.summary().keys()
    assert "transactions_count" in transactions.summary().keys()

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