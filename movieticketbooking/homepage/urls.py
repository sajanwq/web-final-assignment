
from django.urls import path
from homepage import views


urlpatterns = [
    path('homepage_render/', views.homepageindex),
    path('loginpage_render/', views.login),
    path('ticketspage_render/', views.ticketsindex)

]