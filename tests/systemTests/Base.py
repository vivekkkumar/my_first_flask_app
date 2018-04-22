"""
BaseTest
A base class to inherit acting as an interface to all test files.
"""

from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        self.app.testing = True
        self.app = app.test_client