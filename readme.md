# Python Project

A simple Python project with CI/CD setup.

## Features

- Automated testing with pytest
- Code linting with flake8
- GitHub Actions CI/CD pipeline

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

```bash
python -m pytest test_app.py -v
```

## Running Linting

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow
├── app.py                  # Main application file
├── test_app.py            # Test file
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request
