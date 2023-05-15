import boto3

def lambda_handler(event, context):
    if 'pathParameters' in event and 'user_id' in event['pathParameters']:
        user_id = event['pathParameters']['user_id']
        client = boto3.resource('dynamodb')
        table = client.Table('users')
        response = table.get_item(
            Key={
                'user_id': user_id
            }
        )
        if 'Item' in response:
            return response['Item']
        else:
            return {
                'statusCode': 404,
                'body': 'User not found'
            }
    else:
        return {
            'statusCode': 400,
            'body': 'Missing user_id in path parameters'
        }
