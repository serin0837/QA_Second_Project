from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app, db
from application.models import Travel

class TestBase(TestCase):
    def createApp(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///dull.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Travel(country = "Greece", month = "July", build = "camping"))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestGenerator(TestBase):
    def testGen(self):
        response = self.client.get(url_for('gen'))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def testIndex(self):
        with requests_mock.mock() as g:
            g.get("http://35.197.49.49:5001/country", text = "Greece")
            g.get("http://35.197.49.49:5002/month", text = "July")
            g.post("http://35.197.49.49:5003/build", text = "Camping")
            
            response = self.client.get(url_for('gen'))
            self.assertNotIn(b"France", response.data)
            self.assertIn(b"July", response.data)
            self.assertIn(b"Camping", response.data)