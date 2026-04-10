import pytest
import csv
from bank_analyzer import get_total_by_type

@pytest.fixture
def sample_csv(tmp_path):
    result: list[dict] = []
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "account_id,amount,type\n"
        "ACC001,2000.00,deposit\n"
        "ACC003,3000.00,withdrawal\n",
        encoding="utf-8",
    )
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)

    return result

def test_correct_total_by_type(sample_csv):
    assert get_total_by_type(sample_csv, "deposit") >= 0
    assert get_total_by_type(sample_csv, "withdrawal") >= 0
    assert get_total_by_type([], "deposit") == 0.0
    assert get_total_by_type([], "withdrawal") == 0.0

