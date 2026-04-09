from pathlib import Path
from bank_analyzer import get_total_by_type
from bank_analyzer import get_top_transaction
import json

def generate_report(transactions:list[dict], output_path: Path) -> None:
    result = {
        "total_deposits": get_total_by_type(transactions, "deposit"),
        "total_withdrawals": get_total_by_type(transactions, "withdrawal"),
        "net_flow": get_total_by_type(transactions, "deposit") - get_total_by_type(transactions, "withdrawal"),
        "top_transaction": get_top_transaction(transactions),
        "transactions_count": len(transactions),
    }

    # создание json файла отчета
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)