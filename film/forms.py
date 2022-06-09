from django import forms
from .models import gateModel


# creating a form
class gateForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = gateModel

        # specify fields to be used
        fields = [
            "moviename",
            "poster",
            "releasedate",
            "shortdesc",
            "longdesc",
            "publishername",
        ]