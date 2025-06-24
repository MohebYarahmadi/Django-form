from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "date"
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "date"
    )
    list_filter = (
        "date", "occupation"
    )
    ordering = ("date",)
    readonly_fields = ("occupation",)

admin.site.register(Form, FormAdmin)
