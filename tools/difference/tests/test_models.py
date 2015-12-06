from django.test import TestCase

from difference.models import get_difference


class TestFunctions(TestCase):

    def test_get_difference(self):
        number = 10
        value = get_difference(number)
        expected_value = 2640

        self.assertEqual(value, expected_value)

    def test_get_difference_invalid(self):
        number = 'hi'
        value = get_difference(number)
        expected_value = None

        self.assertEqual(value, expected_value)
