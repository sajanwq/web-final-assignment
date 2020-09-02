from django.urls import path
from Booking import views


urlpatterns = [
    path('retrieve_path/', views.index),
    path('create_path/', views.createbook),
    path('delete_book/<int:id>', views.delete)
]

