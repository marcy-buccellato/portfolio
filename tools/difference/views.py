import math

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView, DetailView

from difference.forms import DifferenceForm
from difference.models import Difference


class DifferenceView(FormView):
    """
    Allows user to query on a number and see the difference between the sum of 
    the squares of the first n natural numbers and the square of the sum of the 
    same first n natural numbers, where n is guaranteed to be no greater than 
    100.
    """
    form_class = DifferenceForm
    template_name = "difference/index.html"
    success_url = "/difference/detail/"

    # TODO: Move this method to the model and autoset the difference value upon
    # saving.
    def get_difference(self, number):
        """
        Get difference between the sum of the squares and the square of the sums
        for a given number
        """
        sum_of_the_squares = 0
        sum_of_the_numbers = 0
        for x in range(1, number + 1):
            sum_of_the_squares += math.pow(x, 2)
            sum_of_the_numbers += x

        square_of_the_sums = math.pow(sum_of_the_numbers, 2)

        return square_of_the_sums - sum_of_the_squares

    def form_valid(self, form):
        difference, created = Difference.objects.get_or_create(number=form.cleaned_data['number'])
        if created:
            difference.value = self.get_difference(difference.number)

        difference.occurrences += 1
        difference.save()

        return HttpResponseRedirect(reverse('difference_detail', kwargs={'pk': difference.number}))


class DifferenceDetailView(DetailView):
    """
    Display a Difference object.
    """
    model = Difference
    template_name = "difference/detail.html"
