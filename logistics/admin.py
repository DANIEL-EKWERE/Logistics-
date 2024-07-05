from django.contrib import admin
from .models import GetQuote, Subscribe, ContactUs, Video
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


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "subject",
        "message",
    )

    search_fields = (
        "email",
        "name",
        "id",
    )

    ordering = ["name", "email"]



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )

    search_fields = (
        "id",
        "title"
    )


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
