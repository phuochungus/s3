from django.shortcuts import render
import json

from s3 import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


def s3(request):
    aws_config = {
        "bucket": settings.AWS_STORAGE_BUCKET_NAME,
        "access_key": settings.AWS_ACCESS_KEY_ID,
        "secret_access_key": settings.AWS_SECRET_ACCESS_KEY,
        "region": settings.AWS_S3_REGION_NAME,
    }
    aws_config_json = json.dumps(aws_config)
    response = render(request, "s3.html", {"aws_config": aws_config_json})
    response["X-Frame-Options"] = "ALLOW-FROM *"
    return response


@staff_member_required
def s3_auth(request):
    aws_config = {
        "bucket": settings.AWS_STORAGE_BUCKET_NAME,
        "access_key": settings.AWS_ACCESS_KEY_ID,
        "secret_access_key": settings.AWS_SECRET_ACCESS_KEY,
        "region": settings.AWS_S3_REGION_NAME,
    }
    aws_config_json = json.dumps(aws_config)
    response = render(request, "s3.html", {"aws_config": aws_config_json})
    response["X-Frame-Options"] = "ALLOW-FROM *"
    return response
