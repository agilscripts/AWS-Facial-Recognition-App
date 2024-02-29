import boto3

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodbTableName = 'employee'
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
employeeTable = dynamodb.Table(dynamodbTableName)

def lambda_handler(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        response = index_employee_image(bucket, key)
        print(response)
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            faceId = response['FaceRecords'][0]['Face']['FaceId']
            
            # Assuming register_employee function should be called here
            register_employee(faceId, "John", "Doe")
            
    except Exception as e:
        print(e)
        print(f'Error processing employee image {key} from bucket {bucket}.')
        raise e

def index_employee_image(bucket, key):
    response = rekognition.index_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        CollectionId="employees"  # we will create this later
    )
    return response

def register_employee(faceId, firstName, lastName):
    employeeTable.put_item(
        Item={
            'rekognitionId': faceId,
            'firstName': firstName,
            'lastName': lastName
        }
    )
