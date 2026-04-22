import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['detail']['requestParameters']:
        bucket_name = record['bucketName']
        
        try:
            s3.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
            print(f"Secured bucket: {bucket_name}")
        except Exception as e:
            print(f"Error: {str(e)}")