from django.contrib import admin
from .models import TechAssPages,TechAssPageAdmin
# Register your models here.
admin.site.register(TechAssPages, TechAssPageAdmin)