import json
import math

from django.http import JsonResponse
from django.views.generic import FormView

from difference.forms import DifferenceForm

class DifferenceView(FormView):
    """
    Allows user to query on a number and see the difference between the sum of 
    the squares of the first n natural numbers and the square of the sum of the 
    same first n natural numbers, where n is guaranteed to be no greater than 
    100.
    """
    form_class = DifferenceForm

    # TODO: Move this method to a utils file.
    def get_difference(self, number):
        """
        Get difference between the sum of the squares and the square of the sums
        for a given number
        """
        # TODO: Add limit of 100 for a number.
        sum_of_the_squares = 0
        sum_of_the_numbers = 0
        for x in range(1, int(number) + 1):
            sum_of_the_squares += math.pow(x, 2)
            sum_of_the_numbers += x

        square_of_the_sums = math.pow(sum_of_the_numbers, 2)

        return square_of_the_sums - sum_of_the_squares

    def get_context_data(self, **kwargs):
        number = self.request.GET.get('number')
        # TODO: Add error handling to ensure 'number' is numerical.

        context = {
            "datetime": None,
            "value": self.get_difference(number),
            "number": number,
            "occurrences": None
        }

        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
