from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserRegister
from .models import Buyer, Game


def platform_page(request: HttpRequest):
    pagename = "Главная страница"
    context = {
        "pagename": pagename,
    }
    return render(request, "platform.html", context)


def games_page(request: HttpRequest):
    pagename = "Игры"
    games = Game.objects.all()
    list_games = []
    for game in games:
        list_games.append({"title": game.title, "cost": game.cost, "description": game.description})
    context = {
        "pagename": pagename,
        "list_games": list_games,
    }
    return render(request, "games.html", context)


def card_page(request: HttpRequest):
    pagename = "Корзина"
    text = "Извините, Ваша корзина пуста"
    context = {
        "pagename": pagename,
        "text": text,
    }
    return render(request, "card.html", context)


def sign_up_by_django(request: HttpRequest):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # получаю данные
            error = None
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            # обрабатываю данные
            if password != repeat_password:
                error = "Пароли не совпадают."
            elif age < 18:
                error = "Вы должны быть старше 18."
            elif Buyer.objects.filter(name=username):  # поиск в БД уже существующего пользователя
                error = "Пользователь уже существует"
            else:
                Buyer.objects.create(name=username, balance=0.0, age=age)  # добавление в БД нового пользователя
                info["text"] = f"Приветствуем, {username}!"
            info["error"] = error
            info["form"] = form
    else:
        info["form"] = UserRegister()
    return render(request=request, context=info, template_name="registration_page.html")


def sign_up_by_html(request: HttpRequest):
    info = {}
    if request.method == "POST":
        # получаю данные
        error = None
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        # обрабатываю данные
        if password != repeat_password:
            error = "Пароли не совпадают."
        elif int(age) < 18:
            error = "Вы должны быть старше 18."
        elif Buyer.objects.filter(name=username):  # поиск в БД уже существующего пользователя
            error = "Пользователь уже существует"
        else:
            Buyer.objects.create(name=username, balance=0.0, age=age)  # добавление в БД нового пользователя
            info["text"] = f"Приветствуем, {username}!"
        info["error"] = error
        return render(request, context=info, template_name="registration_page.html")
    else:
        return render(request, "registration_page.html")
