from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Привет</h1><br>Перейдите по адресу <b>/about</b>, чтобы прочитать'
                        'информацию о проекте<br><p>Переходите по адресу <b>/my_games</b>, '
                        'чтобы ознакомиться со списком игр</p>')


def about(request):
    return HttpResponse('<h1>Обо мне</h1><br><p>Проект будет представлять собой блог, '
                        'который в дальнейшем будет развит в <b>полноценное<br>'
                        'многопользовательское приложение</b>, с возможностью'
                        'добавлять свои статьи каждому желающему</p>')
