import csv
from pathlib import Path

REQUIRED_COLUMNS = {"account_id", "amount", "type", "date"}

def load_transactions(file_path: Path) -> list[dict]:
    result: list[dict] = []

    if not file_path.exists():
        raise FileNotFoundError(f'Файл не найден: {file_path}')

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("CSV пустой или отсутствует строка заголовков")

        actual_columns = {name.strip() for name in reader.fieldnames if name}
        missing = REQUIRED_COLUMNS - actual_columns
        if missing:
            raise ValueError(
                f"Отсутствуют обязательные колонки: {', '.join(sorted(missing))}"
            )

        for i, row in enumerate(reader, start=2):  # 2 = первая строка после header
            try:
                row["amount"] = float(row["amount"])
            except (TypeError, ValueError):
                raise ValueError(f"Некорректное значение amount в строке {i}: {row['amount']!r}")

            result.append(row)

        if not result:
            raise ValueError("CSV не содержит данных (только заголовки)")

    return result

