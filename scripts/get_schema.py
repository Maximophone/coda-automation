import requests
from config import TABLE_IDS, API_TOKEN, DOC_ID

TABLE_ID = TABLE_IDS["organisations"]  # Replace with your actual table ID

headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}

def get_tables(doc_id):
    url = f'https://coda.io/apis/v1/docs/{doc_id}/tables'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tables = response.json().get('items', [])
        for table in tables:
            print(f"Table ID: {table['id']}, Name: {table['name']}")
        return tables
    else:
        print(f"Error fetching tables: {response.status_code} - {response.text}")
        return []

def get_table_columns(doc_id, table_id):
    url = f'https://coda.io/apis/v1/docs/{doc_id}/tables/{table_id}/columns'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        columns = response.json().get('items', [])
        for column in columns:
            print(f"Column ID: {column['id']}, Name: {column['name']}, Type: {column['type']}")
        return columns
    else:
        print(f"Error fetching columns: {response.status_code} - {response.text}")
        return []

get_tables(DOC_ID)
columns = get_table_columns(DOC_ID, TABLE_ID)
print(columns)
