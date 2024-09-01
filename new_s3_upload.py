#!/usr/bin/env python3
import cgi
import boto3
from botocore.exceptions import NoCredentialsError

# AWS S3 credentials and bucket name
AWS_ACCESS_KEY ='AKIA6ODU5M2XYDOK556G'
AWS_SECRET_KEY = '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'
S3_BUCKET_NAME = 'my-bucket-1411'

# Function to upload file to S3
def upload_to_s3(file_object, filename):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    try:
        s3.upload_fileobj(file_object, S3_BUCKET_NAME, filename)
        return True
    except NoCredentialsError:
        return False

# Main CGI script
def main():
    # Parse form data
    form = cgi.FieldStorage()

    # Check if file data is present
    if 'file' in form:
        fileitem = form['file']

        # Check if the file was uploaded
        if fileitem.filename:
            # Open the file and upload it to S3
            with fileitem.file as f:
                if upload_to_s3(f, fileitem.filename):
                    print("Content-type:text/html\r\n\r\n")
                    print("<html><head><title>File Upload Success</title></head><body>")
                    print("<h2>File Uploaded Successfully to S3!</h2>")
                    print("</body></html>")
                else:
                    print("Content-type:text/html\r\n\r\n")
                    print("<html><head><title>File Upload Failed</title></head><body>")
                    print("<h2>File Upload to S3 Failed!</h2>")
                    print("</body></html>")
        else:
            print("Content-type:text/html\r\n\r\n")
            print("<html><head><title>No File Uploaded</title></head><body>")
            print("<h2>No file was uploaded!</h2>")
            print("</body></html>")
    else:
        print("Content-type:text/html\r\n\r\n")
        print("<html><head><title>No File Uploaded</title></head><body>")
        print("<h2>No file parameter found in form!</h2>")
        print("</body></html>")

if __name__ == '__main__':
    main()

