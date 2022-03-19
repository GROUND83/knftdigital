from django import forms

# from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    title = forms.CharField(initial="")

    project_type = forms.ModelChoiceField(
        required=False,
        empty_label="the Love",
        queryset=models.ProjectType.objects.all(),
    )
    workstype = forms.ModelChoiceField(
        required=False, empty_label="Caligraphy", queryset=models.Type.objects.all()
    )
    # main = forms.BooleanField(required=False)
    # price = forms.DecimalField(required=False)
