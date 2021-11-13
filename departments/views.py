from django.shortcuts import render
from .models import Department


# We return what we want the user to see when directed to this route



def home(request):
    context = {
        'dpts': Department.objects.all()
    }
    return render(request, 'departments/home.html', context)

def about(request):
    return render(request, 'departments/about.html', {'title':'About'})
