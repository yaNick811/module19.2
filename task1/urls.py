from django.urls import path
from .views import create_data, assign_games_to_buyers

urlpatterns = [
    path('create_data/', create_data, name='create_data'),
    path('assign_games/', assign_games_to_buyers, name='assign_games'),
]