import os
from google.cloud import storage


client = storage.Client()
all_buckets = client.list_buckets()


for bucket in all_buckets:
    #Get bucket size in bytes
    os.system(f'gsutil du -s gs://{bucket.name}')
    
