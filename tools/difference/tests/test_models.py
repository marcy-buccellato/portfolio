from django.test import TestCase

from difference.models import Difference, get_difference


class TestModels(TestCase):

    def test_save(self):
        difference = Difference(number=2)
        difference.save()

        self.assertEqual(difference.value, 4)
        self.assertEqual(difference.occurrences, 1)


class TestFunctions(TestCase):

    def test_get_difference(self):
        number = 10
        value = get_difference(number)
        expected_value = 2640

        self.assertEqual(value, expected_value)

    def test_get_difference_invalid(self):
        number = 'hi'

        with self.assertRaises(ValueError):
            get_difference(number)
