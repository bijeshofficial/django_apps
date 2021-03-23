from django.http import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('create/', views.employee_form, name='employee_form'),
    path('<int:id>/update/', views.employee_update, name='employee_update'),
    path('<int:id>/delete/', views.employee_delete, name='employee_delete'),
    path('<int:id>/detail/', views.employee_detail, name='employee_detail')
]
