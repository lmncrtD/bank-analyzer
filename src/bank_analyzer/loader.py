import csv
from pathlib import Path

def load_transactions(file_path: Path) -> list[dict]:
    result: list[dict] = []

    if not file_path.exists():
        raise FileNotFoundError(f'Файл не найден: {file_path}')

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            row['amount'] = float(row['amount'])
            result.append(row)

    return result

