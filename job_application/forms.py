from django import forms


class ApplicationForm(forms.Form):
    """Use send post request from view"""
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)


class ContactForm(forms.Form):
    """Use send post request from view"""
    name = forms.CharField(max_length=80)
    email = forms.CharField(max_length=80)
    message = forms.CharField(max_length=250)
