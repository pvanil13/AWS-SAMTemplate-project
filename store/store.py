import json, os, boto3, uuid

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table(os.environ['TABLE_NAME'])
topic_arn = os.environ['TOPIC_ARN']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item = {
        'id': str(uuid.uuid4()),
        'data': body.get('data', '')
    }
    table.put_item(Item=item)
    sns.publish(TopicArn=topic_arn, Message=f"New object added: {item['id']}")
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Object stored', 'id': item['id']})
    }
