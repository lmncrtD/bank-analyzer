import argparse
from pathlib import Path
from bank_analyzer import load_transactions
from bank_analyzer import TransactionAnalyzer

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Введите путь к файлу который хотите загрузить", required=True)
    parser.add_argument("--output", type=str, help="Введите путь куда хотите сохранить файл", required=False)
    parser.add_argument("--account", type=str, help="Введите счет по которому хотите вывести транзакции", required=False)
    parser.add_argument("--type", type=str, help="Введите тип операции", required=False)
    args = parser.parse_args()
    data_path = Path(__file__).parent.parent.parent
    default_path = data_path / 'data' / 'sample' / "default-report.json"
    default_account = "ACC001"
    default_type = "deposit"
    loader = load_transactions(data_path / args.input)
    transactions = TransactionAnalyzer(loader)
    if args.type:
        transactions.get_total_by_type(args.type)
    else:
        transactions.get_total_by_type(default_type)
    if args.account:
        transactions.get_transactions_by_account(args.account)
    else:
        transactions.get_transactions_by_account(default_account)
    if args.output:
        transactions.generate_report(Path(args.output))
    else:
        transactions.generate_report(default_path)
    summary = transactions.summary()
    print("\n" + "=" * 3 + " Bank Transaction Analyzer " + "=" * 3)
    print(f"Total deposits: {summary['total_deposits']:,.2f}")
    print(f"Total withdrawals: {summary['total_withdrawals']:,.2f}")
    print(f"Net flow: {summary['net_flow']:,.2f}")
    print(f"Transaction count: {summary['transactions_count']}")
    print("Top transactions: \n", [f"{top['account_id']} | {top['type']} | {float(top['amount']):,.2f} | {top['date']}"
           for top in summary['top_transaction']])
    print(f"Report saved to: {args.output or default_path}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ошибка: {e}")