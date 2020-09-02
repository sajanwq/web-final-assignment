from django.urls import path
from customers import views


urlpatterns = [
    path('retrieve_path/', views.index),
    path('delete_customer/<int:p_id>', views.delete),
    path('signup/', views.create, name="signup users")


]