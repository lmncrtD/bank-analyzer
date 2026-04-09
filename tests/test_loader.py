import csv
from pathlib import Path

import pytest
from bank_analyzer import load_transactions

@pytest.fixture
def sample_csv(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "account_id, amount, type\n"
        "ACC001,2000.00,deposit\n"
        "ACC003,3000.00,withdrawal\n",
        encoding="utf-8",
    )
    return csv_file

def test_load_file_csv(sample_csv):
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        load_transactions(Path("test_fake.csv")) # Выдаст ошибку потому что файл не будет найден.

def test_validate_fields(sample_csv):
    #Проверяем вхождение полей в загруженные данные
    load = load_transactions(sample_csv)
    assert "account_id" in load
    assert "amount" in load
    assert "type" in load
    # Сделаем проверку на то, что содерижмое загруженного файла соответствует структуре
    assert load == [
        {"account_id": "ACC001", "amount": "2000.00", "type": "deposit"},
        {"account_id": "ACC002", "amount": "3000.00", "type": "withdrawal"}
    ]

def test_correct_csv_file(sample_csv):
    # Тестирование выходных типов данных для loader
    load = load_transactions(sample_csv)
    assert isinstance(load, list)
    assert isinstance(load[0], dict)


def test_amount_correct_type(sample_csv):
    # Тестирование поля amount что загружается тип float
    load = load_transactions(sample_csv)
    assert isinstance(load[0]['amount'], float)