import unittest
from unittest.mock import patch, Mock
import json
import io
from client3 import getDataPoint, getRatio  # Replace with your code file name

class TestFinancialMarketSimulation(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_getDataPoint(self, mock_urlopen):
        # Mock the response from the server
        mock_response = io.StringIO(json.dumps([
            {
                'stock': 'ABC',
                'top_bid': {'price': '100'},
                'top_ask': {'price': '102'}
            },
            {
                'stock': 'DEF',
                'top_bid': {'price': '50'},
                'top_ask': {'price': '52'}
            }
        ]))
        mock_urlopen.return_value = Mock()
        mock_urlopen.return_value.read.return_value = mock_response.getvalue()

        # Call the function and check the output
        result = getDataPoint({
            'stock': 'ABC',
            'top_bid': {'price': '100'},
            'top_ask': {'price': '102'}
        })
        self.assertEqual(result, ('ABC', 100.0, 102.0, 101.0))

    def test_getRatio(self):
        # Test when price_b is not zero
        ratio = getRatio(100.0, 50.0)
        self.assertEqual(ratio, 2.0)

        # Test when price_b is zero (should handle this case gracefully)
        ratio = getRatio(100.0, 0)
        self.assertIsNone(ratio)

if __name__ == '__main__':
    unittest.main()
