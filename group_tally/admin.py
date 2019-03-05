from django.contrib import admin
from django import forms
from django.db import models

# Register your models here.
from .models import Record, Person


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'all_members',
                    'date', 'cost', 'average_cost')
    search_fields = ('name',)

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }


admin.site.register(Record, RecordAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'expense')
    search_fields = ('name',)


admin.site.register(Person, PersonAdmin)
