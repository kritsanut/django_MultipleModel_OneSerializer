from django.contrib import admin
from .models import ModelMain


class ModelMainAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'icon_thumbnail',
        'icon',
        'published',
        'added_by',
        'created_date',
    ]

    list_display = (
        'name', 'icon_thumbnail', 'icon', 'published', 'added_by', 'created_date')

    readonly_fields = ['created_date']

    class Meta:
        model = ModelMain


admin.site.register(ModelMain, ModelMainAdmin)
