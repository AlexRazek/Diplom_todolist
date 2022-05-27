from django.contrib import admin

from core.models import User


# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

# @admin.register(User)
class DataAdmin(admin.ModelAdmin):
    exclude = ("password",)
    readonly_fields = ("date_joined", "last_joined")
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("email", "first_name", "last_name", "username")


admin.site.register(User)