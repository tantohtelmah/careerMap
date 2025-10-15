import boto3, os
from werkzeug.utils import secure_filename

def upload_to_s3(file, user_id):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    bucket = os.getenv("AWS_S3_BUCKET")
    filename = secure_filename(f"user_{user_id}_resume_{file.filename}")
    s3.upload_fileobj(file, bucket, filename, ExtraArgs={"ContentType": file.content_type})

    file_url = f"https://{bucket}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{filename}"
    return file_url
