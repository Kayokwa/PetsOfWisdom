from django.contrib import admin

# Register your models here.

from .models import Pets

@admin.register(Pets)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']
