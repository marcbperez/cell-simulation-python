#!/usr/bin/env python
# coding: utf-8

import unittest

from main import *
from main.app import App


class AppTest(unittest.TestCase):
    def setUp(self):
        self.simulation = App(True)

    def test_app(self):
        self.assertIsInstance(self.simulation, App)
