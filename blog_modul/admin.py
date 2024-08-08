from django.contrib import admin
from . import models
# Register your models here.

class admin_blog(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':['title']
    }
    list_display = ['__str__','date','category','slug']
    list_filter = ['date','category']
    list_editable = ['date','category']


admin.site.register(models.Blog_model)
admin.site.register(models.Blog_category)
admin.site.register(models.Blog_comment)


