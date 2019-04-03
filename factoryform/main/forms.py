from django import forms
from django.forms import formset_factory

from datetime import datetime, timezone, timedelta


class ModularCapsuleForm(forms.Form):
    UNIT_CHOICES=((0,'minutes'),(1,'days'),(2,'months'),(3,'years'))
    title = forms.CharField(max_length=250)
    emails = forms.CharField(max_length=2500, required=False)
    twitter = forms.BooleanField(required=False)
    facebook = forms.BooleanField(required=False)
    private = forms.BooleanField(required=False)
    deadman_switch = forms.BooleanField(required=False)
    deadman_counter=forms.IntegerField(required=False)
    deadman_time_unit=forms.ChoiceField(required=False,choices=UNIT_CHOICES)


class ModuleForm(forms.Form):
    description = forms.CharField(max_length=250)
    release_date = forms.DateTimeField()
    file = forms.FileField(required=False)

    def clean_release_date(self):
        data = self.cleaned_data['release_date']
        if data <= datetime.now(timezone.utc):
            raise forms.ValidationError('The release date must be in the future')
        return data


ModulesFormSet = formset_factory(ModuleForm, extra=1, max_num=10)




