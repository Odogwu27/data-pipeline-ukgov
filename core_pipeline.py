import json
import requests
from datetime import datetime
from azure.storage.blob import BlobServiceClient

# 1. Fetch live data from the official UK Government API
print("Connecting to live UK Government data feed...")
url = "https://www.gov.uk"

response = requests.get(url)
market_data = response.json()

# 2. Setup the unique execution file logging parameters
execution_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"raw_uk_gov_data_{execution_timestamp}.json"
json_data_string = json.dumps(market_data, indent=4)

# 3. Secure connection to Azure Storage
# 🚨 SECURITY MASK APPLIED FOR PUBLIC VERSION CONTROL
AZURE_CONNECTION_STRING = "YOUR_SECURE_AZURE_CONNECTION_STRING_HERE"
CONTAINER_NAME = "raw-data-landing"

try:
    print("Initializing secure connection to Azure Storage...")
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=filename)
    
    print(f"Uploading file '{filename}' directly to cloud container...")
    blob_client.upload_blob(json_data_string, overwrite=True)
    print("🚀 SUCCESS! Data pipeline Phase 1 completed perfectly.")
    
except Exception as e:
    print(f"❌ PIPELINE ERROR: {str(e)}")
