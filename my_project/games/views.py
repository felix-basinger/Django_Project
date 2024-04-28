from django.shortcuts import render
from django.http import HttpResponse
import random


def my_games(request):
    return HttpResponse("<h1>Введите в адресной строке выбранную игру: /coin, /dice, /random</h1>")


def coin(request):
    sides = ['Орёл', 'Решка']
    return HttpResponse(f'<h1>{sides[random.randint(0, 1)]}</h1><br>Обновите страницу,'
                        f'чтобы подбросить монетку ещё раз!')


def dice(request):
    return HttpResponse(f'<h1>Сторона кости со значением: <b>{random.randint(1, 6)}</b></h1><br>'
                        f'Обновите страницу, чтобы кинуть кость еще раз')


def random_num(request):
    return HttpResponse(f'<h1>Число: <b>{random.randint(0, 100)}</b></h1><br>'
                        f'Обновите страницу, чтобы получить новый результат')
