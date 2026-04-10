import json
import pytest

@pytest.fixture
def sample_json(tmp_path):
    file = tmp_path / "sample.json"
    report = {
        "total_deposits": 31000.0,
        "total_withdrawals": 5000.0,
        "net_flow": 13000,
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