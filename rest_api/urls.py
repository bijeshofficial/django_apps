from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.api_detail_view, name="api_detail"),
    path('create/', views.api_add_view, name="api_add"),
    path('update/<int:id>/', views.api_update_view, name="api_update"),
    path('delete/<int:id>/', views.api_delete_view, name="api_delete")
]
