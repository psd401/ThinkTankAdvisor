import awsgi2
from server.app import app

def lambda_handler(event, context):
    print(event)
    return awsgi2.response(app, event, context)