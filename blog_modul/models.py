from django.db import models
from jalali_date import *
from home_model.models import Home
from django.contrib.auth.admin import UserAdmin
class Blog_category(models.Model):
    title_category = models.CharField(max_length=30, verbose_name=' نام دسته بندی')
    url = models.CharField(max_length=40, verbose_name='ادرس')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title_category

class Blog_model(models.Model):
    title = models.CharField(max_length=30, verbose_name='موضوع')
    short_description = models.CharField(max_length=50, verbose_name='توضیح کوتاه')
    list_description = models.CharField(max_length=100, default='', verbose_name='توضیحات بلاگ لیست')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image_blog/%Y/%b', verbose_name='عکس')
    category = models.ForeignKey(Blog_category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    date = models.DateField(auto_now_add=True, verbose_name='تاریخ')
    slug = models.SlugField(default='', blank=True, null=True, unique=True)
    blog_preview = models.BooleanField(default=False, verbose_name='پیش نمایش بلاگ')

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'

    def __str__(self):
        return self.title

    def get_jalali_data(self):
        return date2jalali(self.date).strftime('%d %b %Y')


class Blog_comment(models.Model):
    user=models.CharField(max_length=30,verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    image=models.ImageField(upload_to='blog_comment/%Y/%b',blank=True,null=True,default='',verbose_name='عکس')
    text = models.TextField(verbose_name='پیام شما')
    blog = models.ForeignKey(Blog_model, on_delete=models.CASCADE, verbose_name='بلاگ')
    replace = models.ForeignKey('Blog_comment', blank=True, null=True, on_delete=models.CASCADE, verbose_name='پاسخ')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید ادمین')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'



    def get_jalali_data(self):
        return date2jalali(self.create_date).strftime('%d %b %Y')

    def get_jalali_time(self):
        return datetime2jalali(self.create_date).strftime('%H:%M %p')