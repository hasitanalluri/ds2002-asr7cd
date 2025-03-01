#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/hasitanalluri/ds2002-asr7cd/blob/main/labs/lab4/script2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[13]:


import boto3
import requests
import os
from urllib.parse import urlparse
import argparse

# Fetch and save file from the internet
def download_file(fileurl):
  response = requests.get(fileurl)
  filename = os.path.basename(urlparse(fileurl).path)
  with open(filename, 'wb') as f:
    f.write(response.content)
    print("Downloaded", filename)
    return filename

# Upload the file to a bucket in S3
def upload_file_s3bucket(filename, bucket_name, s3_key):
  s3 = boto3.client('s3')
  s3.upload_file(filename, bucket_name, s3_key)
  print("Uploaded", filename, "to", bucket_name, "as", s3_key)

# Presign the file with an expiration time, output presigned URL
def generate_presigned_url(bucket_name, s3_key, expiration):
  s3 = boto3.client('s3')
  url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': s3_key}, ExpiresIn=expiration)
  print(f"Presigned URL generated:", url)
  return url

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("fileurl")
  parser.add_argument("bucket_name")
  parser.add_argument("s3_key")
  parser.add_argument("expiration", type=int)

  args = parser.parse_args()

  filename = download_file(args.fileurl)
  upload_file_s3bucket(filename, args.bucket_name, args.s3_key)
  generate_presigned_url(args.bucket_name, args.s3_key, args.expiration)

if __name__ == "__main__":
    main()

