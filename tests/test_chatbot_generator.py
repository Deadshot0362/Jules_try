import unittest
from scripts.chatbot_generator import generate_chatbot_from_text

class TestChatbotGenerator(unittest.TestCase):

    def test_generate_chatbot_from_text(self):
        # Sample text
        text = """
Hello
This is a test
"""

        # Generate the chatbot
        chatbot = generate_chatbot_from_text(text)

        # Assert that the chatbot was generated correctly
        expected_chatbot = {
            'hello': 'Hello',
            'this': 'This is a test'
        }
        self.assertEqual(chatbot, expected_chatbot)

if __name__ == '__main__':
    unittest.main()
