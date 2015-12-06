from django import forms

from difference.models import Difference


class DifferenceForm(forms.Form):
    number = forms.IntegerField(max_value=100)
