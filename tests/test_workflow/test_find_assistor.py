"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""

import pytest
from synspot import set_default_data_path
from synspot.tests.test_workflow import testing_data
from synspot.tests.test_workflow.Train_helper_function import Train_helper_function


class Test_unread_request(Train_helper_function):

    def test_unread_request(self):
        self.first_user_login()
        self.clean_db()
        self.find_assistor()
