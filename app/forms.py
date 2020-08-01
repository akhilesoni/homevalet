from django import forms

class search(forms.Form):
    servise_type = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    
class add_service(forms.Form):
    name = forms.CharField(max_length=100)
    servise_type = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    price = forms.IntegerField()