from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_country(self):
        with patch("random.choice") as r:
            r.return_value = "Greece"
            response = self.client.get(url_for('country'))
            self.assertEqual(b'Greece', response.data)