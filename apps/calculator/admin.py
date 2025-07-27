from django.contrib import admin

from .models import Operation


class OperationAdmin(admin.ModelAdmin):
    list_display = (
        "operation_id",
        "user_id",
        "parameters",
        "result",
        "inclusion",
    )
    list_display_links = ("user_id",)
    search_fields = (
        "user_id",
        "inclusion",
    )
    list_filter = (
        "user_id",
    )
    list_per_page = 10
    ordering = ("user_id",)


admin.site.register(Operation, OperationAdmin)
