import csv
import random
from datetime import datetime, timedelta

# CSV file path
csv_file_path = 'stgContractDetails.csv'

# Column headers based on the API response
headers = [
    'RecordId', 'BatchId', 'ContractID', 'AgentID', 'CarrierCD', 'AffiliateCD',
    'ContractName', 'ContractFromDate', 'ContractToDate', 'ContractStatus',
    'ContractStatusDate', 'Reason', 'ReasonDate', 'SourceSystem', 'Comments',
    'AS_Contract_GUID', 'LoadDateTime', 'NPN', 'PayeeID', 'MarkerID',
    'AgentProfileID'
]

# Generate sample data
def generate_record(record_id):
    base_date = datetime(2021, 1, 1)
    from_date = base_date + timedelta(days=random.randint(0, 365))
    to_date = from_date + timedelta(days=random.randint(30, 365))
    
    return {
        'RecordId': f'{record_id:06d}',
        'BatchId': f'INB.AML{random.randint(100000, 999999)}',
        'ContractID': f'CON-{random.randint(1000000, 9999999)}',
        'AgentID': f'{random.randint(10000000, 99999999)}',
        'CarrierCD': f'CARRIER{random.randint(1, 50)}',
        'AffiliateCD': f'AFF{random.randint(100, 999)}',
        'ContractName': f'Contract_{record_id}',
        'ContractFromDate': from_date.strftime('%Y-%m-%d'),
        'ContractToDate': to_date.strftime('%Y-%m-%d'),
        'ContractStatus': random.choice(['ACTIVE', 'PENDING', 'INACTIVE']),
        'ContractStatusDate': (from_date + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
        'Reason': random.choice(['ANTHEM - BROKERAGE', 'RENEWAL', 'AMENDMENT']),
        'ReasonDate': (from_date + timedelta(days=random.randint(1, 60))).strftime('%Y-%m-%d'),
        'SourceSystem': random.choice(['TEST01', 'PROD01', 'AGENYSYNC']),
        'Comments': f'Comment_{record_id}',
        'AS_Contract_GUID': f'{random.randint(0, 9999999999999)}-{random.randint(0, 9999999999999)}',
        'LoadDateTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        'NPN': f'NPN{random.randint(1000000000, 9999999999)}',
        'PayeeID': f'PAYEE{random.randint(100000, 999999)}',
        'MarkerID': f'MKR{random.randint(10000, 99999)}',
        'AgentProfileID': f'PROF{random.randint(100000, 999999)}'
    }

# Write CSV file
print("Generating 100k records...")
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    
    for i in range(1, 100001):
        record = generate_record(i)
        writer.writerow(record)
        if i % 10000 == 0:
            print(f"  {i} records written...")

print(f"✓ CSV file created successfully: {csv_file_path}")
print(f"✓ Total records: 100,000")
