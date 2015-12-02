import json

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

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = {
            "datetime": None,
            "value": None,
            "number": self.request.GET.get('number'),
            "occurrences": None
        }

        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
