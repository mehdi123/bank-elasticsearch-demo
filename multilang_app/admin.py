from django.contrib import admin
from .models import MultiModel
# Register your models here.

#admin.register(MultiModel)
admin.register(MultiModel)(admin.ModelAdmin)
