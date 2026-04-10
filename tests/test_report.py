import json
import pytest

@pytest.fixture
def sample_json(tmp_path):
    file = tmp_path / "sample.json"
    report = {
        "total_deposits": 31000.0,
        "total_withdrawals": 5000.0,
        "net_flow": 26000.00,
        "top_transaction": [
            {
                "account_id": "ACC005",
                "amount": 1000.00,
                "type": "deposit",
                "date": "2026-04-01"
            },
            {
                "account_id": "ACC003",
                "amount": 1000.00,
                "type": "withdrawal",
                "date": "2026-04-01"
            }
        ],
        "transactions_count": 9
    }
    with open(file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

    return file

def test_correct_json(sample_json):
    with open(sample_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data is not None

def test_fields_on_json(sample_json):
    with open(sample_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "total_deposits" in data.keys()
    assert "total_withdrawals" in data.keys()
    assert "net_flow" in data.keys()
    assert "top_transaction" in data.keys()
    assert "transactions_count" in data.keys()


def test_correct_values_type_json(sample_json):
    with open(sample_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data['total_deposits'], float)
    assert isinstance(data['total_withdrawals'], float)
    assert isinstance(data['net_flow'], float)
    assert isinstance(data['top_transaction'], list)
    assert isinstance(data['transactions_count'], int)
    assert isinstance(data['top_transaction'][0]['amount'], float)
    assert isinstance(data['top_transaction'][0]['date'], str)
    assert isinstance(data['top_transaction'][0]['type'], str)
    assert isinstance(data['top_transaction'][0]['account_id'], str)

def test_correct_values_json(sample_json):
    with open(sample_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data['net_flow'] is not None
    assert data['net_flow'] == (data['total_deposits'] - data['total_withdrawals'])
    assert data['top_transaction'] is not None
    assert data['transactions_count'] >= 0
    assert data['total_deposits'] >= 0
    assert data['total_withdrawals'] >= 0
    assert data['top_transaction'][0]['amount'] >= 0

