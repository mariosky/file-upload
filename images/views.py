from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import boto3
import pathlib
from uuid import uuid4

# Create your views here.


@csrf_exempt
def upload_start(request):
    try:
        data = json.loads(request.body)
        print(data)
        # Use the data here
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    file_name = file_generate_name(data['file_name'])
    
    presigned_data = s3_generate_presigned_post(file_path=file_name,file_type=data['file_type'])
    return JsonResponse(presigned_data)
    
@csrf_exempt
def upload_finish(request):
    try:
        data = json.loads(request.body)
        print(data)
        # Use the data here
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'message': 'Success'})


def s3_generate_presigned_post(*, file_path: str, file_type: str):
    s3_client = boto3.client( service_name="s3")

    acl = 'private'
    expires_in = 100

    presigned_data = s3_client.generate_presigned_post(
        's3-web-tijuana',
        file_path,
        Fields={
            "acl": acl,
            "Content-Type": file_type
        },
        Conditions=[
            {"acl": acl},
            {"Content-Type": file_type},
        ],
        ExpiresIn=expires_in,
    )

    return presigned_data

def file_generate_name(original_file_name):
    extension = pathlib.Path(original_file_name).suffix

    return f"{uuid4().hex}{extension}"