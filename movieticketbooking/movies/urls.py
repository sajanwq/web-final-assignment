
from django.urls import path
from movies import views


urlpatterns = [
    path('retrieve_path/', views.index),
    path('add_movie/', views.create),
    path('edit_movie/<int:m_id>', views.edit),
    path('update_movie/<int:p_id>', views.update),
    path('delete_movie/<int:id>', views.delete),
    path('moviepage_retrieve/', views.datamovie)
   # path('ticketpage_retrieve/<int:c_id>', views.ticketmovie)

]