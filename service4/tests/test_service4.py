from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestBuild(TestBase):
    def test_jan(self):
        response = self.client.post(url_for('build'), data = "January",)
        self.assertIn(b"enjoy sun", response.data)
    
    def test_feb(self):
        response = self.client.post(url_for('build'), data = "February",)
        self.assertIn(b"enjoy sun", response.data)
    
    def test_mar(self):
        response = self.client.post(url_for('build'), data = "March",)
        self.assertIn(b"enjoy flower", response.data)
    
    def test_april(self):
        response = self.client.post(url_for('build'), data = "April",)
        self.assertIn(b"enjoy flower", response.data)
    
    def test_may(self):
        response = self.client.post(url_for('build'), data = "May",)
        self.assertIn(b"love your partner more", response.data)
    
    def test_june(self):
        response = self.client.post(url_for('build'), data = "June",)
        self.assertIn(b"surfing", response.data)
    
    def test_july(self):
        response = self.client.post(url_for('build'), data = "July",)
        self.assertIn(b"camping", response.data)
    
    def test_august(self):
        response = self.client.post(url_for('build'), data = "August",)
        self.assertIn(b"birthday party", response.data)
    
    def test_sep(self):
        response = self.client.post(url_for('build'), data = "September",)
        self.assertIn(b"read a lot", response.data)
        
    def test_octo(self):
        response = self.client.post(url_for('build'), data = "October",)
        self.assertIn(b"drink beer a lot", response.data)
    
    def test_nov(self):
        response = self.client.post(url_for('build'), data = "November",)
        self.assertIn(b"look back your year", response.data)

    def test_dec(self):
        response = self.client.post(url_for('build'), data = "December",)
        self.assertIn(b"enjoy your life", response.data)
    def test_else(self):
        response = self.client.post(url_for('build'), data = "yay",)
        self.assertIn(b"Build not compatible", response.data)