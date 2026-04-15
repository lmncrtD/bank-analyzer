## Bank-analayzer
Universal CLI Transaction Handler

---
## How to install
pip install -e .

---
## How to use
1) **bash:**\
```alias bank_analyzer='python -m bank_analyzer```

2) **bash:**\
```bank_analyzer --input data/sample/transactions.csv --output data/sample/report.json --type deposit --account ACC001```

3) **bash:**\
```bank_analyzer --help``` - Check commands

4) **Commands:** \
``--input`` - path to the file you want to upload\
``--output`` - the path where you want to save the file\
``--account`` - the account through which we issue transactions\
``--type`` - type of operation
---

## Project Structure
bank-analyzer/\
├── data/\
│ └── sample/\
│ └─── transactions.csv\
├── src/\
│ └── bank_analyzer/\
│ ├─── init.py\
│ ├─── main.py\
│ ├─── analyzer.py\
│ └─── loader.py\
├── tests/\
│ ├── init.py\
│ ├── test_analyzer.py\
│ └── test_loader.py\
├── pyproject.toml
├── README.md
└── .gitignore

---
## Example Input/Output
### Example Input
**bash:**\
``bank_analyzer --input data/sample/transactions.csv --output data/sample/report.json --type deposit --account ACC001``

### Example Output
31000.0\
[{'account_id': 'ACC001', 'amount': 5000.0, 'type': 'deposit', 'date': '2026-04-01'}, {'account_id': 'ACC001', 'amount': 1500.0, 'type': 'withdrawal', 'date': '2026-04-02'}, {'account_id': 'ACC001', 'amount': 2000.0, 'type': 'deposit', 'date': '2026-04-03'}]\
[{'account_id': 'ACC003', 'amount': 10000.0, 'type': 'deposit', 'date': '2026-04-01'}, {'account_id': 'ACC005', 'amount': 10000.0, 'type': 'deposit', 'date': '2026-04-01'}]

===Bank Transaction Analyzer===\
Total deposits: 31,000.00\
Total withdrawals: 5,000.00\
Net flow: 26,000.00\
Transaction count: 9\
Top transactions: \
 ['ACC003 | deposit | 10,000.00 | 2026-04-01', 'ACC005 | deposit | 10,000.00 | 2026-04-01']\
Report saved to: data/sample/report.json