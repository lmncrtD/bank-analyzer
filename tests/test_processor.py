import pytest
import csv
from bank_analyzer import get_total_by_type
from bank_analyzer import get_transactions_by_account
from bank_analyzer import get_top_transaction

@pytest.fixture
def sample_csv(tmp_path):
    result: list[dict] = []
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "account_id,amount,type\n"
        "ACC001,2000.00,deposit\n"
        "ACC003,3000.00,withdrawal\n"
        "ACC001,4000.00,deposit\n"
        "ACC004,100000.00,withdrawal\n"
        "ACC001,100000.00,deposit\n",
        encoding="utf-8",
    )
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)

    return result

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
        {"account_id": "ACC001", "amount": "2000.00", "type": "deposit"},
        {"account_id": "ACC001", "amount": "4000.00", "type": "deposit"},
        {"account_id": "ACC001", "amount": "100000.00", "type": "deposit"}
    ]
    assert "ACC003" not in get_transactions_by_account(sample_csv, "ACC001")
    assert len(get_transactions_by_account(sample_csv, "ACC001")) == 3

def test_top_transactions(sample_csv):
    assert get_top_transaction(sample_csv) == [
        {"account_id": "ACC004", "amount": "100000.00", "type": "withdrawal"},
        {"account_id": "ACC001", "amount": "100000.00", "type": "deposit"}
    ]