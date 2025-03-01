#!/bin/bash

FILE_NAME=$1
BUCKET_NAME=$2
EXPIRATION=$3

# Upload file to private bucket 
aws s3 cp "$FILE_NAME" "s3://$BUCKET_NAME/"

# Presigns a URL to that file with an expiration
PRESIGNED_URL=$(aws s3 presign --expires-in "$EXPIRATION" "s3://$BUCKET_NAME/$FILE_NAME")

echo "$PRESIGNED_URL"
