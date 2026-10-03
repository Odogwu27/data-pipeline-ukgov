import json
import requests
import pandas as pd
from azure.storage.blob import BlobServiceClient

print("🔄 Starting Phase 5: Silver Layer Data Transformation...")

# 1. Establish secure cloud connection parameters
AZURE_CONNECTION_STRING = "YOUR_SECURE_AZURE_CONNECTION_STRING_HERE"
SOURCE_CONTAINER = "raw-data-landing"
TARGET_CONTAINER = "cleaned-data"

try:
    # 2. Connect to the Azure Data Lake
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(SOURCE_CONTAINER)
    
    # 3. Automatically locate your uploaded JSON raw file
    blob_list = list(container_client.list_blobs())
    latest_blob = sorted(blob_list, key=lambda x: x.name)[-1]
    print(f"📥 Extracting latest raw file: {latest_blob.name}")
    
    blob_client = container_client.get_blob_client(latest_blob.name)
    raw_data = json.loads(blob_client.download_blob().readall())
    
    # 4. Standard SQL/Relational Flattening Logic (The Data Mapping)
    events_list = raw_data["england-and-wales"]["events"]
    df = pd.DataFrame(events_list)
    
    # Clean and rename standard database columns
    df = df.rename(columns={"title": "HolidayName", "date": "HolidayDate", "bunting": "IsBuntingFlag"})
    
    # 5. Export cleaned structure directly back to the cloud 'cleaned-data' container
    output_filename = latest_blob.name.replace("raw_uk_gov_data_", "silver_cleaned_data_")
    output_csv = df.to_csv(index=False)
    
