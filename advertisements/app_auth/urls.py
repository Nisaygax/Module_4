from django.urls import path
from .views import login_view, profile_view, register_view, logout_view

urlpatterns = [
    path('profile/', profile_view, name = 'profile'),
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name = 'register'),
    path('logout/', logout_view, name = 'logout')
]