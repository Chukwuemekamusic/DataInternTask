import sys
import os
import pandas as pd
from dotenv import load_dotenv
from pyairtable import Api

# Load environment variables
load_dotenv()

# Get environment variables and check if they exist
api_key = os.getenv('API_KEY')
base_id = os.getenv('BASE_ID')
instagram_table_id = os.getenv('TABLE_ID')

if not all([api_key, base_id, instagram_table_id]):
    raise ValueError("Missing required environment variables. Check your .env file.")

# Initialize API and table
api = Api(api_key)
table = api.table(base_id, instagram_table_id)

def load_file(file_path):
    """Load and validate the CSV file."""
    try:
        # Attempt to read the file
        df = pd.read_csv(file_path)
        
        # Ensure required columns are present
        required_columns = ['Month', 'Year', 'Net Follower Growth', 'Number of Followers', 'Total Engagement', 'Total Impressions', 'Total Video Views']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            raise ValueError(
                f"The file is missing required columns: {', '.join(missing_columns)}.\n"
                f"Expected structure: {', '.join(required_columns)}"
            )

        # # Fill NaN values with default values (e.g., 0)
        # df = df.fillna(0)
        # return df

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist. Please check the path and try again.")

    except Exception as e:
        raise ValueError(f"Error loading file: {e}")

# Main script execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script-name.py <file-path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Load and validate the file
        df = load_file(file_path)

        # Fetch existing records and store unique 'ID' fields (e.g., '{Month}-{Year}')
        existing_records = {record['fields'].get('ID') for record in table.all()}

        # Iterate over DataFrame rows and create records in Airtable
        for index, row in df.iterrows():
            record_data = row.to_dict()

            # Remove computed field if present
            if 'Net Follower Growth' in record_data:
                del record_data['Net Follower Growth']

            # Check if the record already exists in Airtable
            unique_id = f"{record_data['Month']} {record_data['Year']}"
            if unique_id in existing_records:
                print(f"Skipping record {unique_id} as it already exists")
                continue

            # Create the record in Airtable
            try:
                table.create(record_data)
                print(f"Created record: {unique_id}")
            except Exception as e:
                print(f"Error creating record for row {index}: {e}")

        # Print all records for verification
        print("All records in the table:")
        print(table.all())

    except Exception as e:
        print(f"An error occurred: {e}")
