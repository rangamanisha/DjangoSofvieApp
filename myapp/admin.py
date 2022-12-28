from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(StateModel)
class StateModelAdmin(admin.ModelAdmin):
    list_display = ("name",)[::-1]


@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("state", "dob", "company_name")[::-1]



@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ("name", "state")[::-1]
