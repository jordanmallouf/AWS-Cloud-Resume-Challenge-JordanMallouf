import boto3
import json
from decimal import Decimal

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("VisitorCounter")

# Helper function to convert Decimal to native Python types
def decimal_to_native(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def lambda_handler(event, context):
    # Get the current visitor count from DynamoDB
    response = table.get_item(Key={'id': '0'})
    views = response.get('Item', {}).get('views', 0)

    # Increment the visitor count
    views += 1

    # Update the visitor count in DynamoDB
    table.put_item(Item={'id': '0', 'views': views})

    # Return the updated visitor count with proper serialization
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
        },
        'body': json.dumps({'views': views}, default=decimal_to_native)
    }
