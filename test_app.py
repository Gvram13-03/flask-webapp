from flask import Flask
import unittest

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, DevOps World!'

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, DevOps World!')

if __name__ == '__main__':
    unittest.main()