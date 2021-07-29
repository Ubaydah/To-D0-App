from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<str:pk>/', views.UpdateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.DeleteTask, name='delete_task'),
]