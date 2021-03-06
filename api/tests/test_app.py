"""Tests that predictions are working.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: test_app.py
     Package: api.tests
     Created on 10 July, 2019 @ 02:42 PM.

   @license
     BSD-3 Clause license.
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""
import unittest
from api.app import app


class TestApp(unittest.TestCase):
    def test_app(self):
        app.testing = True
        client = app.test_client()

        response = client.get('/')
        assert response.status_code == 200
