import os
from google.cloud import storage


client = storage.Client()
all_buckets = client.list_buckets()


for bucket in all_buckets:
    #Only select non-testin buckets, and add policy.
    if bucket.labels['session'] != 'qa-testing':
        #Strip first 3 characters and last 2 characters from bucket name.
        project_number = bucket.name[3:-2]
        role = 'roles/storage.objectViewer'
        member = f'{project_number}-compute@developer.gserviceaccount.com'
        policy = f'gsutil iam ch serviceAccount:{member}:{role} gs://{bucket.name}'
        output = os.system(policy)
