from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, DateTimeBaseInput, CheckboxSelectMultiple, CheckboxInput, RadioSelect, TimeInput
from django.utils import timezone
from main.models import Sith, Planet, Recruit, Questions


class RecruitForm(ModelForm):
    class Meta:
        model = Recruit
        fields = ['name', 'planet', 'age', 'email']


class SelectSith(forms.Form):
    sith = forms.ChoiceField(label='Выбор Ситха', required=False)