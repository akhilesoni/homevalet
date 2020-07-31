from django import forms

class search(forms.Form):
    servise_type = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    