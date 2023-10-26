# pip install -r requirements.txt

import boto3
import logging

# Get handle to high-level S3 resource
s3 = boto3.resource('s3')
buckets = [bucket.name for bucket in s3.buckets.all()]
num = len(buckets)

# Make sure we found at least one bucket
if (num <= 0):
    print("Sorry, you have no S3 buckets")
    exit()

# List buckets
print("Here are your", num, "S3 buckets")
print('=' * 40)
for i,bucket in enumerate(buckets):
    print(i+1, '-', bucket)

# Prompt user input num
choice = 0
while (choice < 1 or choice > num):
    print("Enter a bucket number (1-" + str(num) + "): ", end="")
    choice = int(input())

# Fetch the bucket's objects
bucketName = buckets[choice-1]
bucket = s3.Bucket(bucketName)
objects = bucket.objects

# Iterate through all the objects
print("\nList the objects in bucket", bucketName)
print('=' * 60)
for obj in objects.all():
    print(obj.key, "-", obj.size, "bytes")

print("\nDone.")
