from django.shortcuts import render
from .models import Department
from django.views.generic import ListView, DetailView


# We return what we want the user to see when directed to this route


def home(request):
    context = {
        'dpts': Department.objects.all()
    }
    return render(request, 'departments/home.html', context)


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/home.html'
    context_object_name = 'dpts'
    ordering = ['name']


class DepartmentDetailView(DetailView):
    model = Department


def about(request):
    return render(request, 'departments/about.html', {'title':'About'})
