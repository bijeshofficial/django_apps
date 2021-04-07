from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='function_index'),
    path('create_musician/', views.create_musician, name='create_musician'),
    path('create_album/', views.create_album, name='create_album'),
    path('update_musician/<int:id>/',
         views.update_musician, name='update_musician'),
    path('update_album/<int:id>/',
         views.update_album, name='update_album'),
    path('delete_musician/<int:id>/',
         views.delete_musician, name='delete_musician'),
    path('delete_album/<int:id>/',
         views.delete_album, name='delete_album'),
]
