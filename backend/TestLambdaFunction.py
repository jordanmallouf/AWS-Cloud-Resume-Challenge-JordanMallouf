import unittest
from unittest.mock import MagicMock
import lambda_function
import json

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):
        # Mock DynamoDB
        lambda_function.dynamodb = MagicMock()
        mock_table = lambda_function.dynamodb.Table("VisitorCounter")
        mock_table.get_item.return_value = {'Item': {'views': 42}}
        mock_table.put_item.return_value = {}

        # Simulate event and context
        event = {}
        context = {}

        response = lambda_function.lambda_handler(event, context)

        # Assert response
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('views', json.loads(response['body']))
