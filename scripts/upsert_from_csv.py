import requests
import csv
import argparse
from column_mappings import MAPPINGS, KEY_COLUMNS
from config import API_TOKEN, DOC_ID, TABLE_IDS

CSV_FILE_PATH = 'test_contacts.csv'  # Replace with the path to your CSV file
TABLE_NAME = "contacts"
COLUMNS_MAPPING = MAPPINGS[TABLE_NAME]
KEY_COLUMNS = KEY_COLUMNS[TABLE_NAME]
TABLE_ID = TABLE_IDS[TABLE_NAME]

# Coda API Headers
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

def read_csv_file(csv_file_path):
    """Reads the CSV file and returns data as a list of dictionaries."""
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def prepare_rows(data, columns_mapping):
    """Maps CSV data to Coda columns and formats it appropriately."""
    rows = []
    for record in data:
        cells = []
        for field_name, value in record.items():
            if field_name in columns_mapping and value:
                column_info = columns_mapping[field_name]
                column_id = column_info['column_id']
                column_type = column_info['column_type']

                # Handle different column types
                if 'lookup' in column_type:
                    # Assume values are semicolon-separated for multiple items
                    value = [item.strip() for item in value.split(';')]
                elif column_type == 'checkbox':
                    value = value.lower() in ('true', '1', 'yes')
                elif column_type == 'date':
                    # Convert date string to appropriate format if necessary
                    pass  # Skipping date formatting for simplicity
                elif column_type == 'select':
                    value = value.strip()
                else:
                    value = value.strip()

                cell = {'column': column_id, 'value': value}
                cells.append(cell)
        rows.append({'cells': cells})
    return rows

def upsert_rows(doc_id, table_id, rows_data, key_columns):
    """Uses the Coda API to upsert rows into the specified table."""
    url = f'https://coda.io/apis/v1/docs/{doc_id}/tables/{table_id}/rows'
    key_column_ids = [COLUMNS_MAPPING[key]['column_id'] for key in key_columns]
    payload = {
        'rows': rows_data,
        'keyColumns': key_column_ids
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 202:
        print("Rows upserted successfully.")
        return response.json()
    else:
        print(f"Error upserting rows: {response.status_code} - {response.text}")
        return None

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Upsert data from a CSV file to Coda.")
    parser.add_argument("csv_file", help="Path to the CSV file to be processed")
    args = parser.parse_args()

    # Use the provided CSV file path
    csv_file_path = args.csv_file

    # Step 1: Read data from CSV file
    data = read_csv_file(csv_file_path)
    print(f"Read {len(data)} records from CSV file.")

    # Step 2: Prepare rows for upserting
    rows_data = prepare_rows(data, COLUMNS_MAPPING)
    print(f"Prepared {len(rows_data)} rows for upserting.")

    # Step 3: Upsert rows into Coda
    upsert_rows(DOC_ID, TABLE_ID, rows_data, KEY_COLUMNS)

if __name__ == '__main__':
    main()
