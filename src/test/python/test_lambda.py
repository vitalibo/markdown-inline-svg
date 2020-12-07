import importlib
import json

import pytest

app = importlib.import_module('src.main.python.lambda')


@pytest.fixture()
def apigw_event():
    ''' Generates API GW Event'''

    return {
        'body': '{ "test": "body"}',
        'resource': '/{proxy+}',
        'requestContext': {
            'resourceId': '123456',
            'apiId': '1234567890',
            'resourcePath': '/{proxy+}',
            'httpMethod': 'POST',
            'requestId': 'c6af9ac6-7b61-11e6-9a41-93e8deadbeef',
            'accountId': '123456789012',
            'identity': {
                'apiKey': '',
                'userArn': '',
                'cognitoAuthenticationType': '',
                'caller': '',
                'userAgent': 'Custom User Agent String',
                'user': '',
                'cognitoIdentityPoolId': '',
                'cognitoIdentityId': '',
                'cognitoAuthenticationProvider': '',
                'sourceIp': '127.0.0.1',
                'accountId': '',
            },
            'stage': 'prod',
        },
        'queryStringParameters': {
        },
        'headers': {
            'Via': '1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)',
            'Accept-Language': 'en-US,en;q=0.8',
            'CloudFront-Is-Desktop-Viewer': 'true',
            'CloudFront-Is-SmartTV-Viewer': 'false',
            'CloudFront-Is-Mobile-Viewer': 'false',
            'X-Forwarded-For': '127.0.0.1, 127.0.0.2',
            'CloudFront-Viewer-Country': 'US',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'X-Forwarded-Port': '443',
            'Host': '1234567890.execute-api.us-east-1.amazonaws.com',
            'X-Forwarded-Proto': 'https',
            'X-Amz-Cf-Id': 'aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==',
            'CloudFront-Is-Tablet-Viewer': 'false',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Custom User Agent String',
            'CloudFront-Forwarded-Proto': 'https',
            'Accept-Encoding': 'gzip, deflate, sdch',
        },
        'pathParameters': {'proxy': '/examplepath'},
        'httpMethod': 'POST',
        'stageVariables': {'baz': 'qux'},
        'path': '/examplepath',
    }


def test_handler_ok(apigw_event, mocker):
    apigw_event['queryStringParameters'] = {
        'source': 'https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md',
        'name': 'sample.svg'
    }

    ret = app.handler(apigw_event, '')

    assert ret['statusCode'] == 200
    assert 'Content-Type' in ret['headers']
    assert ret['headers']['Content-Type'] == 'image/svg+xml'
    assert ret['body'].startswith('<?xml version="1.0" encoding="UTF-8"?>')
    assert ret['body'].endswith('</svg>')


def test_handler_bad_request_missing_param_source(apigw_event, mocker):
    apigw_event['queryStringParameters'] = {
        'name': 'sample.svg'
    }

    ret = app.handler(apigw_event, '')

    assert ret['statusCode'] == 400
    data = json.loads(ret["body"])
    assert data['message'] == 'Missing required parameter: source'


def test_handler_bad_request_missing_param_name(apigw_event, mocker):
    apigw_event['queryStringParameters'] = {
        'source': 'https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md'
    }

    ret = app.handler(apigw_event, '')

    assert ret['statusCode'] == 400
    data = json.loads(ret["body"])
    assert data['message'] == 'Missing required parameter: name'


def test_handler_bad_request_incorrect_schema(apigw_event, mocker):
    apigw_event['queryStringParameters'] = {
        'source': 'foo',
        'name': 'sample.svg'
    }

    ret = app.handler(apigw_event, '')

    assert ret['statusCode'] == 400
    data = json.loads(ret["body"])
    assert 'Invalid URL' in data['message']


def test_handler_internal_server_error(apigw_event, mocker):
    apigw_event['queryStringParameters'] = {
        'source': 'https://foo',
        'name': 'sample.svg'
    }

    ret = app.handler(apigw_event, '')

    assert ret['statusCode'] == 500
    data = json.loads(ret["body"])
    assert 'Failed to establish a new connection' in data['message']


if __name__ == '__main__':
    pytest.main(['-v'])
