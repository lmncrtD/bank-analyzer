import argparse
from pathlib import Path
from bank_analyzer import load_transactions
from bank_analyzer import TransactionAnalyzer

def main() -> None:
    '''Добавить прием аргументов из командой строки используя argparse'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Введите путь к файлу который хотите загрузить")
    parser.add_argument("--output", type=str, help="Введите путь куда хотите сохранить файл")
    parser.add_argument("--account", type=str, help="Введите счет по которому хотите вывести транзакции")
    parser.add_argument("--type", type=str, help="Введите тип операции")
    args = parser.parse_args()
    data_path = Path(__file__).parent.parent.parent
    if not args.input:
        raise ValueError("Передай --input, например: --input data/transactions.json")
    loader = load_transactions(data_path / args.input)
    transactions = TransactionAnalyzer(loader)
    print(transactions.get_total_by_type(args.type))
    print(transactions.get_transactions_by_account(args.account))
    print(transactions.get_top_transaction())
    transactions.generate_report(Path(args.output))
    summary = transactions.summary()
    print("\n" + "=" * 3 + " Bank Transaction Analyzer " + "=" * 3)
    print(f"Total deposits: {summary['total_deposits']:,.2f}")
    print(f"Total withdrawals: {summary['total_withdrawals']:,.2f}")
    print(f"Net flow: {summary['net_flow']:,.2f}")
    print(f"Transaction count: {summary['transactions_count']}")
    print("Top transactions: \n", [f"{top['account_id']} | {top['type']} | {float(top['amount']):,.2f} | {top['date']}"
           for top in summary['top_transaction']])
    print(f"Report saved to: {args.output}")

if __name__ == "__main__":
    main()