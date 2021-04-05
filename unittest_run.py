from flaskdemo import app
import unittest

class AppTest(unittest.TestCase):
    def test_response(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()