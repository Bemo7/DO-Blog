import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "do-deelers"
AWS_S3_ENDPOINT_URL="https://fra1.digitaloceanspaces.com"
AWS_LOCATION = f"https://{AWS_BUCKET_NAME}.fra1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "do_deelers.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "do_deelers.cdn.backends.StaticRootS3Boto3Storage"