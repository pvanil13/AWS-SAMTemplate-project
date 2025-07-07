import os, boto3, json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.scan()
    items = response.get('Items', [])
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }

