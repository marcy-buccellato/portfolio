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
    template_name = "difference/input.html"

    def form_valid(self, form):
        difference, created = Difference.objects.get_or_create(
            number=form.cleaned_data['number'])
        # Update difference object: increase occurrences, update date, set
        # value if new.
        difference.save()

        return HttpResponseRedirect(reverse('difference_detail',
                                            kwargs={'pk': difference.number}))


class DifferenceDetailView(DetailView):
    """
    Display a Difference object.
    """
    model = Difference
    template_name = "difference/detail.html"
