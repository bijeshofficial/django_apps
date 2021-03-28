from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ajax_index'),
    path('book_add/', views.book_add, name='book_add'),

]
