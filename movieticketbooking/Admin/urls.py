
from django.urls import path
from Admin import views


urlpatterns = [
    path('retrieve_path/', views.index),
    path('create_path/', views.create),
    path('edit_path/<int:p_id>', views.edit),
    path('update_path/<int:p_id>', views.update),
    path('delete_path/<int:d_id>', views.delete)
]