from django.contrib import admin
from .models import *
# Register your models here.

class admin_blog(admin.ModelAdmin):
    list_display = ['__str__','category']
    list_filter = ['title','category']
    list_editable = ['title','category']


admin.site.register(Portfolio)
admin.site.register(PortfolioCategory)