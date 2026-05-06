from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_record, name='add_record'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
]
