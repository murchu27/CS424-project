from django.contrib import admin

# Register your models here.
from .models import Production


class ProductionAdmin(admin.ModelAdmin):
    list_display= ['name','date_time']
    sortable_by= ['date_time']

admin.site.register(Production,ProductionAdmin)
