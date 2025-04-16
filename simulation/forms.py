from django import forms

class SimulationForm(forms.Form):
    url = forms.URLField()
    simulations = forms.IntegerField(min_value=1)