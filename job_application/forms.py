from django import forms


class ApplicationForm(forms.Form):
    """docstring for ApplicationForm."""

    def __init__(self, arg):
        super(ApplicationForm, self).__init__()
        self.arg = arg

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
