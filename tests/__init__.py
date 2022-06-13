"""Tests for the app."""

from config import Config
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class TestConfig(Config):
    TESTING = True