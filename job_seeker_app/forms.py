from django import forms
from django.contrib.auth.models import User
from .models import Personals, Professionals, Academics, Degree


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class PersonalsForm(forms.ModelForm):
    class Meta:
        model = Personals
        fields = "__all__"


class ProfessionalsForm(forms.ModelForm):
    class Meta:
        model = Professionals
        fields = "__all__"


class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academics
        # fields ="__all__"
        fields = ['board', 'degree', 'institution', 'result', 'year', 'user_id']



class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = "__all__"
