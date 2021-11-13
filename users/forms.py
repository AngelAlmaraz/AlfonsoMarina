from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from departments.models import Department

class UserRegisterForm(UserCreationForm):
    # fields = Department.objects.all()
    email = forms.EmailField()
    dpt_list = list(Department.objects.values_list())
    choices = [(str(i[0]), i[1]) for i in dpt_list]
    department = forms.MultipleChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ['username','email','department','password1','password2']