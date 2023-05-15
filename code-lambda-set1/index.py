import boto3
import uuid

def lambda_handler(event, context):
    ddbClient = boto3.resource('dynamodb')
    ddbTable = ddbClient.Table('users')
    
    if 'user_id' not in event:
        event['user_id'] = str(uuid.uuid4())
        
    response = ddbTable.put_item(
        Item={
            'user_id': event['user_id'],
            'name': event['name'],
            'birthday': event['birthday']
        }
    )
    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': 'Record ' + event['user_id'] + ' Added'
    }
