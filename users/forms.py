from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from departments.models import Department

class UserRegisterForm(UserCreationForm):
    # fields = Department.objects.all()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']