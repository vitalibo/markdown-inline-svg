import json
import urllib.error
import urllib.request


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

        request = urllib.request.Request(params['source'], headers=headers)
        with urllib.request.urlopen(request) as response:
            text = response.read().decode('utf-8')

        name = f"@{params['name']}"
        body = text[text.find(name) + len(name):text.rfind(name)].strip()

        return {
            'statusCode': 200,
            'body': body,
            'headers': {
                'Content-Type': 'image/svg+xml'
            }
        }

    except Exception as e:
        return {
            'statusCode': 400 if isinstance(e, ValueError) else 500,
            'body': json.dumps({
                'message': str(e)
            })
        }
