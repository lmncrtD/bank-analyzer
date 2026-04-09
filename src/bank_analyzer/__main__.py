from pathlib import Path
from bank_analyzer import get_top_transaction
from bank_analyzer import get_total_by_type
from bank_analyzer import get_transactions_by_account
from bank_analyzer import generate_report
from bank_analyzer import load_transactions

def main() -> None:
    data_path = Path(__file__).parent.parent.parent
    loader = load_transactions(data_path / "data" / "sample" / "transactions.csv")
    print(get_total_by_type(loader, 'deposit'))
    print(get_transactions_by_account(loader, 'ACC001'))
    print(get_top_transaction(loader))
    print(data_path / "data" / "sample")
    generate_report(loader, data_path / "data" / "sample" / "report.json")

if __name__ == "__main__":
    main()