from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = (
        'name',
        'color'
    )

    search_fields = (
        'name',
    )


@admin.register(Task)
class Tasks(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
    )



