"""
Testing simple cases for Xls2Json
"""
import sys, os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.test import TestCase, Client
from json2xform.xls2json import ExcelToJsonConverter

class BasicXls2JsonApiTests(TestCase):

    def test_simple_yes_or_no_question(self):
        x = ExcelToJsonConverter("json2xform/surveys/super_simple/yes_or_no_question.xls")
        x_results = x.to_dict()
        
        expected_dict = {u'survey': [{u'list name': u'yes_or_no', u'text': {u'english': u'have you had a good day today?'}, u'type': u'select one', u'name': u'good_day'}], u'choices': {u'yes_or_no': [{u'text': {u'english': u'yes'}, u'value': u'yes'}, {u'text': {u'english': u'no'}, u'value': u'no'}]}}
        
        self.assertEqual(x_results, expected_dict)


    def test_gps(self):
        x = ExcelToJsonConverter("json2xform/surveys/super_simple/gps.xls")

        expected_dict = {u'survey': [{u'type': u'gps', u'name': u'location'}], u'choices': {}}

        self.assertEqual(x.to_dict(), expected_dict)

    
    def test_string_and_integer(self):
        x = ExcelToJsonConverter("json2xform/surveys/super_simple/string_and_integer.xls")

        expected_dict = {u'survey': [{u'text': {u'english': u'What is your name?'}, u'type': u'string', u'name': u'your_name'}, {u'text': {u'english': u'How many years old are you?'}, u'type': u'integer', u'name': u'your_age'}], u'choices': {}}

        self.assertEqual(x.to_dict(), expected_dict)
