def lambda_handler(event, context):
    token = event['authorizationToken']
    if token == "allow":
        return {
            "principalId": "user123",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [{
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow123456",
                    "Resource": event['methodArn']
                }]
            }
        }
    else:
        raise Exception("Unauthorized")

