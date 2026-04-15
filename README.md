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
===Bank Transaction Analyzer===\
Total deposits: 31,000.00\
Total withdrawals: 5,000.00\
Net flow: 26,000.00\
Transaction count: 9\
Top transactions: \
 ['ACC003 | deposit | 10,000.00 | 2026-04-01', 'ACC005 | deposit | 10,000.00 | 2026-04-01']\
Report saved to: data/sample/report.json