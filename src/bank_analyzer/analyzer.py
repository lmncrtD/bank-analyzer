import json
from pathlib import Path

class TransactionAnalyzer:
    def __init__(self, transactions: list[dict]):
        self.transactions: list[dict] = transactions

    def get_total_by_type(self, tx_type: str) -> float:
        result = 0.0
        for transaction in self.transactions:
            if transaction["type"] == tx_type:
                result += float(transaction["amount"])

        return result

    def get_transactions_by_account(self, account_id: str) -> list[dict]:
        result: list[dict] = []
        for transaction in self.transactions:
            if transaction["account_id"] == account_id:
                transaction["amount"] = float(transaction["amount"])
                result.append(transaction)

        return result

    def get_top_transaction(self) -> list[dict] | None:
        max_amount = max(float(t['amount']) for t in self.transactions)
        return [t for t in self.transactions if float(t['amount']) == max_amount]

    def summary(self) -> dict:
        deposit = self.get_total_by_type("deposit")
        withdrawals = self.get_total_by_type("withdrawal")
        result = {
            "total_deposits": deposit,
            "total_withdrawals": withdrawals,
            "net_flow": deposit - withdrawals,
            "top_transaction": self.get_top_transaction(),
            "transactions_count": len(self.transactions),
        }
        return result

    def generate_report(self, output_path: Path) -> None:
        # создание json файла отчета
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.summary(), f, indent=4, ensure_ascii=False)