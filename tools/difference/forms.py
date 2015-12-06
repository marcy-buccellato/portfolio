from django import forms


class DifferenceForm(forms.Form):
    """
    Form to input a number to be calculated.
    """
    number = forms.IntegerField(max_value=100)
