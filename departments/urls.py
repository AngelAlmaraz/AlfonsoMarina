from django.urls import path
from . import views
from .views import DepartmentListView, DepartmentDetailView


urlpatterns = [
    path('', DepartmentListView.as_view(), name = 'departments-home'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name = 'departments-detail'),
    path('about/', views.about, name = 'departments-about'),
]