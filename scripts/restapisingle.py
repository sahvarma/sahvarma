import json
import time
from datetime import datetime
import pandas as pd
import requests

csv_path = r"C:\Users\sahvarma\Pictures\AmeriLife\sahvarma\stgContractDetails.csv"
endpoint = "https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer icm-UtmrpIOmG+F2TKcazvBjVy9qik0cUlq+YEtXwThauNM=",
    "Model": "AmeriLifeDev"
}
send_single_record = True

start_time = datetime.now()
start_timestamp = time.time()
print(f"Start: {start_time.isoformat()}")

try:
    df = pd.read_csv(csv_path)
except Exception as exc:
    print(f"Failed to read CSV: {exc}")
    raise

rows_source = df.head(1) if send_single_record else df
payload = {
    "rows": rows_source.fillna("").astype(str).values.tolist(),
       "inputFormId":1
}

print(f"Sending {len(payload['rows'])} row(s) in payload")
print(json.dumps(payload, indent=2)[:2000])  # show the first part of the payload for debugging

try:
    response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
    print(f"Response status: {response.status_code}")
    print(response.text)
except Exception as exc:
    print(f"Request failed: {exc}")
    raise

end_time = datetime.now()
end_timestamp = time.time()
print(f"End: {end_time.isoformat()}")
print(f"Duration seconds: {end_timestamp - start_timestamp:.3f}") 
#To read the CSV file and send an API response to the Varicent system, you can use Python with the `pandas` library to read the CSV file and the `requests` library to make the POST request. Below is an example code snippet that demonstrates how to achieve this: