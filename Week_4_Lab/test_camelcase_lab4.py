"""This file contains a list of unit tests to ensure that the program functions correctly when handling unusual inputs."""

import camelCase_lab4
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('theQuickBrownFoxJumps', camelCase_lab4.camel_case('The quick brown fox jumps')) 
        # tests an expected input

        self.assertEqual('theQuickBrownFoxJumps', camelCase_lab4.camel_case('         The         quick brown fox         jumps')) 
        # this test is used to ensure that all spaces are ignored

        self.assertEqual('theQuickBrownFoxJumps', camelCase_lab4.camel_case('The . quick ! brown @ fox  ** ^^^&&&`~ `=+ jumps 88'))
        # this test checks to make sure that special characters are ignored

        self.assertEqual('', camelCase_lab4.camel_case('😁😛😋🤣'))
        # this test checks to ensure that if emojis are inputted an empty string is returned

        self.assertEqual('', camelCase_lab4.camel_case(''))
        # this test checks to ensure that an empty string is returned if an empty string is inputted