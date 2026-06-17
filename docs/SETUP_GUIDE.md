# AmeriLife Setup Guide

## Prerequisites

- Python 3.7 or higher
- pip package manager
- Git (optional)

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/sahvarma/sahvarma.git
cd sahvarma
```

### 2. Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env` file in project root:

```env
API_ENDPOINT=https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows
AUTH_TOKEN=your_bearer_token_here
API_MODEL=AmeriLifeDev
TIMEOUT=60
BATCH_SIZE=2000
LOG_LEVEL=INFO
```

### 5. Verify Installation

```bash
python scripts/import_csv.py --help
python scripts/rest_api_single.py --help
python scripts/rest_api_bulk.py --help
```

## Quick Start

1. **Generate test data:**
   ```bash
   python scripts/import_csv.py
   ```

2. **Test single record:**
   ```bash
   python scripts/rest_api_single.py
   ```

3. **Submit batch (dry run):**
   ```bash
   python scripts/rest_api_bulk.py --dry-run
   ```

4. **Submit batch (actual):**
   ```bash
   python scripts/rest_api_bulk.py
   ```

## Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues.
