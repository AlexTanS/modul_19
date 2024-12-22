from django.contrib import admin
from .models import Buyer, Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ("size", "cost",)  # фильтрация
    list_display = ("title", "cost", "size",)  # поля отображения списком
    search_fields = ("title",)  # поле для поиска
    list_per_page = 20  # ограничение количества записей на странице


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ("balance", "age",)
    list_display = ("name", "balance", "age")
    search_fields = ("name",)
    list_per_page = 30
    readonly_fields = ("balance",)  # только для чтения
