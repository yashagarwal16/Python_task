#!/usr/bin/env python3

import cgi
import os
import cgitb
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

cgitb.enable()

# Load environment variables
load_dotenv()

# AWS credentials from environment variables
AWS_ACCESS_KEY_ID ='AKIA6ODU5M2XYDOK556G'
AWS_SECRET_ACCESS_KEY ='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'
AWS_REGION ='ap-south-1'
AWS_S3_BUCKET ='my-bucket-1411'

# HTML response headers
print("Content-Type: text/html")
print()

def upload_to_s3(fileitem):
    try:
        s3 = boto3.client('s3', region_name=AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        s3.put_object(Bucket=AWS_S3_BUCKET,
                      Key=fileitem.filename,
                      Body=fileitem.file,
                      ContentType=fileitem.type)
        
        return f"File uploaded successfully: {fileitem.filename}"

    except NoCredentialsError:
        return "Credentials not available"

# Parse form data
form = cgi.FieldStorage()

if 'image' in form:
    fileitem = form['image']

    if fileitem.filename:
        message = upload_to_s3(fileitem)
    else:
        message = "No file was uploaded"
else:
    message = "No file was selected"

print(f"""
<html>
<body>
    <h1>{message}</h1>
    <a href="/upload.html">Upload another file</a>
</body>
</html>
""")
