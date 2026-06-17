# AmeriLife Project 🚀

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Private-red)](#license)
[![Status](https://img.shields.io/badge/Status-Active-green)](#)

## Overview

AmeriLife is an enterprise-grade data integration project focused on bulk loading contract details to the Varicent API. This repository contains utilities for CSV data generation, single-record API submission, and batch processing of contract information with advanced error handling and monitoring capabilities.

**Key Use Cases:**
- Generate high-volume test data for contract management systems
- Perform single-record API submissions for validation
- Execute batch operations with automatic retry and splitting logic
- Monitor and track data loading operations

## 📁 Project Structure

```
AmeriLife/
├── README.md                          # Project documentation (this file)
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python package dependencies
├── LICENSE                            # Project license
│
├── scripts/
│   ├── __init__.py                    # Package initialization
│   ├── import_csv.py                  # CSV data generation utility (100k records)
│   ├── rest_api_single.py             # Single record API submission
│   ├── rest_api_bulk.py               # Batch processing with retry logic
│   └── config.py                      # Configuration management
│
├── data/
│   └── stgContractDetails.csv         # Sample contract details dataset
│
├── tests/
│   ├── __init__.py                    # Test package initialization
│   ├── test_api_submission.py         # API submission tests
│   └── test_data_generation.py        # Data generation tests
│
├── docs/
│   ├── API_DOCUMENTATION.md           # API endpoint documentation
│   ├── SETUP_GUIDE.md                 # Detailed setup instructions
│   └── TROUBLESHOOTING.md             # Common issues and solutions
│
└── config/
    ├── development.env                # Development configuration
    └── production.env                 # Production configuration
```

## ✨ Features

### 1. CSV Data Generation
- **Script:** `import_csv.py`
- Generates 100,000 sample contract records with realistic test data
- Configurable record count and data patterns
- Automatic timestamp generation
- Support for multiple source systems

### 2. Single Record API Submission
- **Script:** `rest_api_single.py`
- Submit individual records for validation
- Detailed response logging
- Error tracking and reporting
- Perfect for testing and debugging

### 3. Bulk Batch Processing
- **Script:** `rest_api_bulk.py`
- Efficiently submit large CSV datasets
- Configurable batch sizes (default: 2000 rows)
- Automatic retry logic for oversized batches (413 errors)
- Binary backoff splitting strategy
- Progress tracking and performance metrics
- Network error handling with graceful degradation

## 🔧 Prerequisites

- **Python:** 3.7 or higher
- **pip:** Python package manager
- **Git:** Version control (optional)

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/sahvarma/sahvarma.git
cd sahvarma
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### 1. Generate Sample Data
```bash
python scripts/import_csv.py
```
**Output:** Creates `data/stgContractDetails.csv` with 100,000 records

**Options:**
```bash
# Specify custom record count
python scripts/import_csv.py --records 50000

# Save to custom location
python scripts/import_csv.py --output custom_path.csv
```

### 2. Submit a Single Record
```bash
python scripts/rest_api_single.py
```
**Action:** Sends the first record from CSV file to test API connection

**Options:**
```bash
# Test with custom CSV file
python scripts/rest_api_single.py --csv-path path/to/file.csv

# Specify record index
python scripts/rest_api_single.py --record-index 0
```

### 3. Batch Submit All Data
```bash
# Default batch size (2000 rows)
python scripts/rest_api_bulk.py

# Custom batch size
python scripts/rest_api_bulk.py --batch-size 500

# Test run without sending requests
python scripts/rest_api_bulk.py --dry-run

# Send only first record for testing
python scripts/rest_api_bulk.py --single

# Verbose logging
python scripts/rest_api_bulk.py --verbose

# Specify custom CSV path
python scripts/rest_api_bulk.py --csv-path data/custom.csv
```

## 🔌 API Configuration

API endpoints and authentication details are configured in `config/` directory:

**Production Endpoint:**
```
https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows
```

**Authentication:**
- Type: Bearer Token
- Model: AmeriLifeDev
- Content-Type: application/json

**Configuration Variables:**
- `API_ENDPOINT` - Varicent API URL
- `AUTH_TOKEN` - Bearer token for authentication
- `API_MODEL` - Varicent model identifier
- `TIMEOUT` - Request timeout (default: 60s)
- `BATCH_SIZE` - Default batch size (default: 2000)

## 📊 Data Schema

The contract details dataset includes the following 21 fields:

| Field | Type | Description |
|-------|------|-------------|
| RecordId | String | Unique record identifier |
| BatchId | String | Batch processing identifier |
| ContractID | String | Unique contract identifier |
| AgentID | String | Agent identifier |
| CarrierCD | String | Carrier code |
| AffiliateCD | String | Affiliate code |
| ContractName | String | Contract name |
| ContractFromDate | Date | Contract start date |
| ContractToDate | Date | Contract end date |
| ContractStatus | Enum | ACTIVE, PENDING, INACTIVE |
| ContractStatusDate | Date | Status change date |
| Reason | String | Contract reason/type |
| ReasonDate | Date | Reason date |
| SourceSystem | String | Source system (TEST01, PROD01, AGENYSYNC) |
| Comments | String | Additional comments |
| AS_Contract_GUID | String | Global unique identifier |
| LoadDateTime | DateTime | Data load timestamp |
| NPN | String | NPN identifier |
| PayeeID | String | Payee identifier |
| MarkerID | String | Marker identifier |
| AgentProfileID | String | Agent profile identifier |

## ⚙️ Error Handling

### Automatic Retry Logic
- **413 Error (Payload Too Large):** Automatically splits batch in half and retries
- **Network Errors:** Logs detailed error messages and stops gracefully
- **Timeout Errors:** Configurable timeout with detailed logging

### Progress Tracking
- Real-time batch processing status
- Record counts with visual progress
- Duration tracking (total and per batch)
- Success/failure ratios

## 🔍 Monitoring & Logging

### Log Levels
- `DEBUG` - Detailed operation information
- `INFO` - General process updates
- `WARNING` - Potential issues
- `ERROR` - Critical failures

### Output Information
```
Start: 2026-06-17T14:00:00.000000
Total rows to send: 100000
Sending batch 1: rows 1-2000 (size=2000)
Response status: 200
...
End: 2026-06-17T14:05:30.000000
Duration seconds: 330.145
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_api_submission.py

# Run with coverage
python -m pytest --cov=scripts tests/
```

## 📖 Additional Documentation

- **[API Documentation](docs/API_DOCUMENTATION.md)** - Detailed API endpoint reference
- **[Setup Guide](docs/SETUP_GUIDE.md)** - Step-by-step installation and configuration
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions

## 🐛 Troubleshooting

### Issue: "Failed to read CSV"
**Solution:** Verify CSV file path and ensure file exists

### Issue: "413 Payload Too Large"
**Solution:** Script automatically handles this by splitting batches. If persists, reduce `--batch-size`

### Issue: "Authorization Failed"
**Solution:** Check Bearer token validity and ensure it's not expired

### Issue: "Connection Timeout"
**Solution:** Check network connectivity and API endpoint availability

For more help, see [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

## 📝 License

This project is private and proprietary to AmeriLife.

## 👤 Author

**sahvarma**
- GitHub: [@sahvarma](https://github.com/sahvarma)
- Repository: [sahvarma/sahvarma](https://github.com/sahvarma/sahvarma)

## 📞 Support

For issues, questions, or contributions, please:
1. Check [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
2. Review existing [issues](https://github.com/sahvarma/sahvarma/issues)
3. Create a new issue if problem persists

## 🔄 Version History

- **v1.0.0** (2026-06-17) - Initial release with core functionality

---

**Last Updated:** 2026-06-17

**Repository:** [sahvarma/sahvarma](https://github.com/sahvarma/sahvarma)