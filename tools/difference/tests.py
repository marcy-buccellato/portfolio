from django.test import TestCase

from difference.views import DifferenceView

# TODO: Create tests directory with a test file for each module, 
# e.g. test_views.py.
class TestViews(TestCase):

	def setUp(self):
		self.view = DifferenceView()

	def test_get_difference(self):
		number = 10
		value = self.view.get_difference(number)
		expected_value = 2640

		self.assertEqual(value, expected_value)
