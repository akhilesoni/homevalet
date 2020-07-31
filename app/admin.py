from django.contrib import admin

# Register your models here.
from app.models import servise

class serviseAdmin(admin.ModelAdmin):
    pass
admin.site.register(servise, serviseAdmin)