from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_resource, name='book_resource'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('register/', views.register, name='register'),
    path("guest-login/", views.guest_login, name="guest_login"),
    path('logout/', views.user_logout, name='logout'),


]
