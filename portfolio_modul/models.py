from django.db import models

# Create your models here.


class PortfolioCategory(models.Model):
    title=models.CharField(max_length=30,verbose_name='عنوان دسته بندی')
    url=models.CharField(max_length=30,verbose_name='ادرس')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    name_project=models.CharField(max_length=30,verbose_name='نام پروژه')
    category=models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE,verbose_name='دسته بندی')
    icon=models.CharField(max_length=50,default='fa fa-image',verbose_name='ایکون')
    image=models.ImageField(upload_to='portfolio/%Y/%b',blank=True,verbose_name='عکس')
    video=models.FileField(upload_to='portfolio/%Y/%b',blank=True,help_text='در این قسمت می توانید ویدیو اضافه کنید',verbose_name='ویدیو')
    slug = models.SlugField(unique=True,blank=True,null=True,default='project',verbose_name='اسلاگ')
    url = models.CharField(max_length=300,null=True,blank=True,verbose_name='ادرس')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'

    def __str__(self):
        return self.name_project