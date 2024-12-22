from django.db import models


class Buyer(models.Model):
    """Модель представляющая покупателя."""
    name = models.CharField(max_length=100)  # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=11, decimal_places=2)  # баланс(DecimalField)
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    """Модель представляющая игру."""
    title = models.CharField(max_length=100)  # название игры
    cost = models.DecimalField(max_digits=11, decimal_places=2)  # цена(DecimalField)
    size = models.DecimalField(max_digits=13, decimal_places=4)  # размер файлов игры(DecimalField)
    description = models.TextField()  # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+ (BooleanField, по умолчанию False)

    # покупатель обладающий игрой (ManyToManyField)
    # у каждого покупателя может быть игра и у каждой игры может быть несколько обладателей
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title
