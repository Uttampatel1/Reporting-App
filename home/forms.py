from django import forms

class DataForm(forms.Form):
    name = forms.CharField(max_length=100)
    start_date = forms.DateField()
    end_date = forms.DateField()
