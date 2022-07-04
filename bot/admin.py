from django.contrib import admin

from bot.models import TgUser


class TgUserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "user", "username")

admin.site.register(TgUser, TgUserAdmin)