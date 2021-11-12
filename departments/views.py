from django.shortcuts import render
from .models import Department


# We return what we want the user to see when directed to this route


#  we generate a bit of context data

dpts = [

    {
    'Dpt_Name': 'Ventas',
    'Contents':'Dummy content'
    },
    {'Dpt_Name': 'Recursos_Humanos',
     'Contents':'Dummy content'
     },
    {'Dpt_Name': 'Marketing',
     'Contents':'Dummy content'
     }
]

def home(request):
    context = {
        'dpts': Department.objects.all()
    }
    return render(request, 'departments/home.html', context)

def about(request):
    return render(request, 'departments/about.html', {'title':'About'})
