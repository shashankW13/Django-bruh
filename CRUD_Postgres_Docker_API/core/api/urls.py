from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('user/<int:pk>', views.getUser),
    path('create/', views.addUser),
    path('update/<int:pk>', views.updateUser),
    path('delete/<int:pk>', views.deleteUser),
]