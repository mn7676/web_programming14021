from django.contrib import admin
from . import models

# Register your models here.

class AdminTest(admin.ModelAdmin):
    list_display = ("firstname", "phone")

admin.site.register(models.Address)
admin.site.register(models.test, AdminTest)
