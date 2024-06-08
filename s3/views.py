from django.shortcuts import render
import json

from s3 import settings

def s3(request):
    aws_config = {
        "bucket": settings.AWS_STORAGE_BUCKET_NAME,
        "access_key": settings.AWS_ACCESS_KEY_ID,
        "secret_access_key": settings.AWS_SECRET_ACCESS_KEY,
        "region": settings.AWS_S3_REGION_NAME,
    }
    aws_config = json.dumps(aws_config)
    return render(request, "s3.html", {"aws_config": aws_config})
