from django import forms

class DifferenceForm(forms.Form):
    number = forms.CharField(max_length=100)
