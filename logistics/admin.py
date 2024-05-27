from django.contrib import admin
from .models import GetQuote, Subscribe
# Register your models here.


@admin.register(GetQuote)
class GetQuoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "firstName",
        "lastName",
        "business",
        "email",
        "city",
        "phone",
        "postalCode",
    )

    search_fields = (
        "email",
        "firstName",
        "lastName",
    )

    ordering = ["firstName", "email"]


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display= (
        "id",
        "email",
        "created",
    )

    search_fields = (
    "email",
    "created"
    )
