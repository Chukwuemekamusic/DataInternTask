from dotenv import load_dotenv
import os
import pandas as pd
from pyairtable import Api

# Load environment variables
load_dotenv()

# Get environment variables and check if they exist
api_key = os.getenv('API_KEY')
base_id = os.getenv('BASE_ID')
instagram_table_id = os.getenv('TABLE_ID')

file_path = '../transformed_wide/social_metrics.csv'

# Debug: Print to verify values are loaded
print(f"API Key exists: {bool(api_key)}")
print(f"Base ID exists: {bool(base_id)}")
print(f"Table ID exists: {bool(instagram_table_id)}")

if not all([api_key, base_id, instagram_table_id]):
    raise ValueError("Missing required environment variables. Check your .env file.")

# Initialize API and table
api = Api(api_key)
table = api.table(base_id, instagram_table_id)

#fetch existing records and store unique 'ID' fields i.e '{month}-{year}'
existing_records = {record['fields'].get('ID') for record in table.all()}

# Load your DataFrame
df = pd.read_csv(file_path)

# Fill NaN values with a default value, e.g., 0 or an empty string
df = df.fillna(0)

# Create a new record from the DataFrame
for index, row in df.iterrows():
    record_data = row.to_dict()
    
    if 'Net Follower Growth' in record_data:
        del record_data['Net Follower Growth']  # Remove the computed field

    if f"{record_data['Month']} {record_data['Year']}" in existing_records:
        print(f"Skipping record {record_data['Month']} {record_data['Year']} as it already exists")
        continue

    try:
        table.create(record_data)
    except Exception as e:
        print(f"Error creating record for row {index}: {e}")

print(table.all())