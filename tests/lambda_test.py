import importlib
import json
import unittest


class TestLambda(unittest.TestCase):

    def setUp(self):
        self.lambda_func = importlib.import_module('src.lambda')
        with open('tests/event.json', 'r', encoding='utf-8') as f:
            self.apigw_event = json.load(f)

    def test_handler_ok(self):
        apigw_event = self.apigw_event.copy()
        apigw_event['queryStringParameters'] = {
            'source': 'https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md',
            'name': 'aws.svg'
        }

        ret = self.lambda_func.handler(apigw_event, '')

        assert ret['statusCode'] == 200
        assert 'Content-Type' in ret['headers']
        assert ret['headers']['Content-Type'] == 'image/svg+xml'
        assert ret['body'].startswith('<?xml version="1.0" encoding="UTF-8"?>')
        assert ret['body'].endswith('</svg>')

    def test_handler_bad_request_missing_param_source(self):
        apigw_event = self.apigw_event.copy()
        apigw_event['queryStringParameters'] = {
            'name': 'aws.svg'
        }

        ret = self.lambda_func.handler(apigw_event, '')

        assert ret['statusCode'] == 400
        data = json.loads(ret["body"])
        assert data['message'] == 'Missing required parameter: source'

    def test_handler_bad_request_missing_param_name(self):
        apigw_event = self.apigw_event.copy()
        apigw_event['queryStringParameters'] = {
            'source': 'https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md'
        }

        ret = self.lambda_func.handler(apigw_event, '')

        assert ret['statusCode'] == 400
        data = json.loads(ret["body"])
        assert data['message'] == 'Missing required parameter: name'

    def test_handler_bad_request_incorrect_schema(self):
        apigw_event = self.apigw_event.copy()
        apigw_event['queryStringParameters'] = {
            'source': 'foo',
            'name': 'aws.svg'
        }

        ret = self.lambda_func.handler(apigw_event, '')

        assert ret['statusCode'] == 400
        data = json.loads(ret["body"])
        assert "unknown url type: 'foo'" in data['message']

    def test_handler_internal_server_error(self):
        apigw_event = self.apigw_event.copy()
        apigw_event['queryStringParameters'] = {
            'source': 'https://foo',
            'name': 'aws.svg'
        }

        ret = self.lambda_func.handler(apigw_event, '')

        assert ret['statusCode'] == 500
        data = json.loads(ret["body"])
        assert 'nodename nor servname provided, or not known' in data['message']


if __name__ == '__main__':
    unittest.main(verbosity=2)
