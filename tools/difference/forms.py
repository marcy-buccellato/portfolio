from django import forms


class DifferenceForm(forms.Form):
    """
    Form to input a number to return the Difference item.
    """
    number = forms.IntegerField(max_value=100)
