from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "name",
        "email",
        "inclusion",
    )
    list_display_links = ("name", "email",)
    search_fields = (
        "user_id",
        "name",
        "email",
    )
    list_filter = (
        "user_id",
        "name",
        "email",
    )
    list_per_page = 10
    ordering = ("name",)


admin.site.register(User, UserAdmin)
