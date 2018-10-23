#!/usr/bin/python

import boto3


s3Client = boto3.client('s3')
s3Resource = boto3.resource('s3')

bucket = "tw-dep-installapplications-test"
#Expiry time is in seconds - 2592000 is 30 days
#expiry = 2592000
#Going for 3 months (ish)
expiry = 7776000

packages_bucket = s3Resource.Bucket(bucket)



for item in packages_bucket.objects.all():
     print item.key
    print(s3Client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item.key}, ExpiresIn = expiry))
