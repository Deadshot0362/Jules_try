import unittest
from unittest.mock import patch
import requests
from scripts.content_extractor import extract_text_from_url

class TestContentExtractor(unittest.TestCase):

    @patch('requests.get')
    def test_extract_text_from_url_success(self, mock_get):
        # Mock the response from requests.get
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body><p>Hello, world!</p></body></html>'
        mock_get.return_value = mock_response

        # Call the function with a dummy URL
        text = extract_text_from_url('http://example.com')

        # Assert that the text was extracted correctly
        self.assertEqual(text.strip(), 'Hello, world!')

    @patch('requests.get')
    def test_extract_text_from_url_failure(self, mock_get):
        # Mock a failed request
        mock_get.side_effect = requests.exceptions.RequestException

        # Call the function with a dummy URL
        text = extract_text_from_url('http://example.com')

        # Assert that the function returns None
        self.assertIsNone(text)

if __name__ == '__main__':
    unittest.main()
