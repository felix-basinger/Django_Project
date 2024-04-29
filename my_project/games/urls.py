from django.urls import path, include
from .views import coin, dice, random_num, my_games

urlpatterns = [
    path('', my_games, name='my_games'),
    path('coin', coin, name='coin'),
    path('dice', dice, name='dice'),
    path('random', random_num, name='random_num'),
]
