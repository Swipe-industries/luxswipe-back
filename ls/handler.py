import json

def hello(event, context):
    allowed_origins = 'http://localhost:3000,https://www.luxswipe.in'
    origin = event.get('headers', {}).get('origin', '')
    
    if origin in allowed_origins.split(','):
        access_control_allow_origin = origin
    else:
        access_control_allow_origin = allowed_origins.split(',')[0]  # Default to the first origin

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': access_control_allow_origin,
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Amz-User-Agent',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Hello from Lambda!')
    }
