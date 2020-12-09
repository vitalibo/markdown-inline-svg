import json

import requests


def handler(event, context):
    try:
        params = event['queryStringParameters']
        for param in 'source', 'name':
            if param not in params:
                raise ValueError(f'Missing required parameter: {param}')

        headers = {}
        if 'token' in params:
            headers = {
                'Authorization': f"token {params['token']}"
            }

        response = requests.get(params['source'], headers=headers)

        text = response.text
        name = f"@{params['name']}"
        body = text[text.find(name) + len(name):text.rfind(name)].strip()

        return {
            'statusCode': 200,
            'body': body,
            'headers': {
                'Content-Type': 'image/svg+xml'
            }
        }

    except (ValueError, requests.RequestException) as e:
        return {
            'statusCode': 400 if isinstance(e, ValueError) else 500,
            'body': json.dumps({
                'message': str(e)
            })
        }
