import os
import boto3
from PIL import Image
from django.conf import settings

# Define AWS credentials and S3 bucket name
# aws_access_key = settings.aws_access_key
# aws_secret_key = settings.aws_secret_key
# s3_bucket_name = settings.s3_bucket_name


# Define AWS credentials and S3 bucket name with local credential 
aws_access_key = ""
aws_secret_key = ""
s3_bucket_name = ""

# Initialize the S3 client
s3 = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# def compress_image(input_path, output_path, quality=95):
#     # Open the image
#     img = Image.open(input_path)
#     print("Hello How are you",img)

#     # Save the image with the desired quality
#     img.save(output_path, "JPEG", quality=quality, optimize=True)

def compress_image(input_path, output_path, quality=95):
    # Open the image
    img = Image.open(input_path)

    # Convert to RGB mode if the image is in RGBA mode
    if img.mode == "RGBA":
        img = img.convert("RGB")

    # Save the image with the desired quality
    img.save(output_path, "JPEG", quality=quality, optimize=True)


def upload_to_s3(local_path, s3_path):
    s3.upload_file(local_path, s3_bucket_name, s3_path)

def main():
    # Specify the directory to traverse
    source_directory = "/home/naseem/naseem_git/celery_redis/awsimage"

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                full_path = os.path.join(root, file)
               

                # Compress the image (optional, you can adjust quality)
                compressed_path = "compressed_" + file
                compress_image(full_path, compressed_path, quality=95)

                # Upload the compressed image to S3
                s3_path = os.path.relpath(full_path, source_directory)
                upload_to_s3(compressed_path, s3_path)

                # Clean up the compressed image
                os.remove(compressed_path)

if __name__ == "__main__":
    main()

