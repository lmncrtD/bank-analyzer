def get_total_by_type(transactions: list[dict], tx_type: str) -> float:
    result = 0.0
    for transaction in transactions:
        if transaction["type"] == tx_type:
            result += float(transaction["amount"])

    return result

def get_transactions_by_account(transactions: list[dict], account_id: str) -> list[dict]:
    result: list[dict] = []
    for transaction in transactions:
        if transaction["account_id"] == account_id:
            transaction["amount"] = float(transaction["amount"])
            result.append(transaction)

    return result

def get_top_transaction(transactions: list[dict]) -> dict | None:
    max_amount = max(float(t['amount']) for t in transactions)
    return [t for t in transactions if float(t['amount']) == max_amount]