# AmeriLife Project

## Overview
AmeriLife is a data integration project focused on bulk loading contract details to the Varicent API. This repository contains utilities for CSV data generation, single-record API submission, and batch processing of contract information.

## Project Structure

```
sahvarma/
├── README.md                    # This file - Project documentation
├── requirements.txt             # Python package dependencies
├── import csv.py               # Generate sample CSV data with 100k contract records
├── restapisingle.py            # Submit a single record to the API
├── restapibulk.py              # Batch submit CSV records to the API
└── stgContractDetails.csv      # Sample contract details data file
```

## Features

- **CSV Data Generation** (`import csv.py`): Generates 100,000 sample contract records with realistic test data
- **Single Record API Submission** (`restapisingle.py`): Send individual records to the AmeriLife Varicent API
- **Bulk Batch Processing** (`restapibulk.py`): Efficiently submit large CSV datasets in configurable batches with automatic retry logic

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository
2. Install required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Generate Sample Data
```bash
python "import csv.py"
```
This generates 100,000 sample contract records and saves them to `stgContractDetails.csv`.

### 2. Submit a Single Record
```bash
python restapisingle.py
```
Sends the first record from the CSV file to test the API connection.

### 3. Submit Data in Batches
```bash
# Send all records with default batch size (2000 rows)
python restapibulk.py

# Custom batch size
python restapibulk.py --batch-size 500

# Test run without sending requests
python restapibulk.py --dry-run

# Send only first record for testing
python restapibulk.py --single
```

### Command-line Options for `restapibulk.py`
- `--batch-size`: Number of rows per batch (default: 2000)
- `--single`: Send only the first row (useful for testing)
- `--dry-run`: Run without sending requests; only print counts

## Configuration

API endpoints and authentication details are configured within the scripts:
- **Endpoint**: `https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows`
- **Model**: AmeriLifeDev
- **Auth**: Bearer token authentication

## Data Schema

The contract details include the following fields:
- RecordId, BatchId, ContractID, AgentID
- CarrierCD, AffiliateCD, ContractName
- ContractFromDate, ContractToDate, ContractStatus
- ContractStatusDate, Reason, ReasonDate
- SourceSystem, Comments, AS_Contract_GUID
- LoadDateTime, NPN, PayeeID, MarkerID, AgentProfileID

## Error Handling

- Automatic retry logic for oversized batches (413 errors)
- Network error handling with detailed error messages
- Progress tracking with record counts

## License

Private repository

## Author

sahvarma
