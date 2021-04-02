from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ajax_2_home'),
    path('save/', views.save_data, name='ajax_2_save'),
    path('delete/', views.delete_data, name="ajax_2_delete"),
]
