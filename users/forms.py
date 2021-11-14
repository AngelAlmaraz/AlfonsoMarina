from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from departments.models import Department
from.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    dpt_list = list(Department.objects.values_list())
    choices = [(str(i[0]), i[1]) for i in dpt_list]
    department = forms.MultipleChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ['username','email','department','password1','password2']


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()
    dpt_list = list(Department.objects.values_list())
    choices = [(str(i[0]), i[1]) for i in dpt_list]
    department = forms.MultipleChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ['username', 'email','department']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']