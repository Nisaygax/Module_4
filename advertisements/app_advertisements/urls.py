from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('', index, name = 'main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('advertisement-post/', top_sellers, name = 'advertisement-post'),
    path('register/', top_sellers, name = 'register'),
    path('login/', top_sellers, name = 'login'),
    path('profile/', top_sellers, name = 'profile'),
]
