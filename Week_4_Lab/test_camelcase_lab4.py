import camelCase_lab4
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self): #

        expected_string = 'theQuickBrownFoxJumps' # create a variable to be tested

        self.assertEqual(expected_string, camelCase_lab4.camel_case('The quick brown fox jumps'))

        self.assertEqual(expected_string, camelCase_lab4.camel_case('         The         quick brown fox         jumps'))

        self.assertEqual(expected_string, camelCase_lab4.camel_case('The . quick ! brown @ fox jumps **')) # TODO: update this

        # TODO: add more tests. Intentionally create incorrect inputs to see if program handles it properly