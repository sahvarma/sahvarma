import argparse
import time
from datetime import datetime
import pandas as pd
import requests

# Configuration
csv_path = r"C:\Users\sahvarma\Pictures\Python\data\stgContractDetails.csv"
endpoint = "https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer icm-UtmrpIOmG+F2TKcazvBjVy9qik0cUlq+YEtXwThauNM=",
    "Model": "AmeriLifeDev",
}


def send_batch(batch_rows, attempt_info=""):
    """Send a single batch (list-of-lists) to the endpoint and return the HTTP status code.

    Raises requests.exceptions.RequestException on network errors.
    """
    payload = {"rows": batch_rows, "inputFormId": 1}
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
        print(f"{attempt_info}Response status: {response.status_code}")
        print(response.text)
        return response.status_code
    except requests.exceptions.RequestException as exc:
        print(f"{attempt_info}Request failed: {exc}")
        raise


def main(batch_size: int, send_single_record: bool, dry_run: bool):
    start_time = datetime.now()
    start_ts = time.time()
    print(f"Start: {start_time.isoformat()}")

    # Read CSV
    try:
        df = pd.read_csv(csv_path)
    except Exception as exc:
        print(f"Failed to read CSV: {exc}")
        raise

    rows_source = df.head(1) if send_single_record else df
    total_rows = len(rows_source)
    print(f"Total rows to send: {total_rows}")

    if dry_run:
        print("Dry run: not sending requests. Exiting.")
        return

    batch_no = 0
    for start in range(0, total_rows, batch_size):
        batch_no += 1
        chunk = rows_source.iloc[start : start + batch_size]
        batch_rows = chunk.fillna("").astype(str).values.tolist()
        sent_range = f"rows {start+1}-{start+len(batch_rows)}"
        print(f"Sending batch {batch_no}: {sent_range} (size={len(batch_rows)})")

        try:
            status = send_batch(batch_rows, attempt_info=f"Batch {batch_no}: ")
        except requests.exceptions.RequestException:
            # On network error, stop or implement retry logic here
            print(f"Batch {batch_no} failed due to network error. Stopping.")
            raise

        # If nginx returns 413, try splitting this batch into smaller sub-batches once
        if status == 413 and len(batch_rows) > 1:
            print(f"Batch {batch_no} too large (413). Splitting into smaller chunks and retrying...")
            # Use binary backoff to find a workable sub-size quickly
            sub_size = max(1, batch_size // 2)
            sub_no = 0
            for s in range(0, len(batch_rows), sub_size):
                sub_no += 1
                sub_rows = batch_rows[s : s + sub_size]
                print(f"  Sending sub-batch {batch_no}.{sub_no}: size={len(sub_rows)}")
                try:
                    send_batch(sub_rows, attempt_info=f"Batch {batch_no}.{sub_no}: ")
                except requests.exceptions.RequestException:
                    print(f"  Sub-batch {batch_no}.{sub_no} failed due to network error. Stopping.")
                    raise

    end_time = datetime.now()
    end_ts = time.time()
    print(f"End: {end_time.isoformat()}")
    print(f"Duration seconds: {end_ts - start_ts:.3f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send CSV rows to Varicent API in batches")
    parser.add_argument("--batch-size", type=int, default=2000, help="number of rows per batch (default: 2000)")
    parser.add_argument("--single", action="store_true", help="send only the first row (useful for testing)")
    parser.add_argument("--dry-run", action="store_true", help="do not send requests; only print counts")
    args = parser.parse_args()

    main(batch_size=args.batch_size, send_single_record=args.single, dry_run=args.dry_run)
