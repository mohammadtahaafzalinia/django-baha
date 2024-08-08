from django.db import models
# Create your models here.
from django.core.validators import MaxValueValidator
from googletrans.client import Translator

class Condition(models.Model):
    title_condition=models.CharField(max_length=50,verbose_name='عنوان')

    def __str__(self):
        return self.title_condition

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'


class Favorites(models.Model):
    Issue=models.CharField(max_length=80,verbose_name='موضوع')
    icon=models.CharField(blank=True,max_length=50,verbose_name='ایکون')

    def __str__(self):
        return self.Issue

    class Meta:
        verbose_name = 'علایق'
        verbose_name_plural = 'علاقه مندی ها'


class Service(models.Model):
    logo_service=models.CharField(max_length=50,verbose_name='لوگو')
    title_service=models.CharField(max_length=30,null=True,verbose_name='عنوان خدمات')
    description_service=models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title_service

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'


class Opinions(models.Model):
    name_opinions=models.CharField(max_length=50,verbose_name='نام ونام خانوادگی')
    image_opinions=models.ImageField(upload_to='image_opinions/%Y/%b',null=True,verbose_name='عکس')
    service_user=models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='نوع خدمات')
    score=models.PositiveIntegerField(default=5,validators=[MaxValueValidator(5)])
    description_opinions=models.TextField(verbose_name='توضیحات')


    def __str__(self):
        return self.name_opinions

    class Meta:
        verbose_name = 'دیگاه مشتری'
        verbose_name_plural = 'دیدگاه مشتریان'


class Prices(models.Model):
    title_prices=models.CharField(max_length=30,verbose_name='عنوان')
    logo_prices=models.CharField(max_length=50,null=True,verbose_name='ایکون')
    price=models.IntegerField(verbose_name='قیمت')
    period_choice=[
        ('ماهانه','ماهانه'),
        ('سالانه','سالانه'),
        ('دورکاری','دورکاری'),
    ]
    period=models.CharField(max_length=50,choices=period_choice,verbose_name='بازه زمانی')

    def __str__(self):
        return self.title_prices

    class Meta:
        verbose_name = 'قیمت'
        verbose_name_plural = 'قیمت ها'


class AboutModel(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام و نام خانوادگی')
    country= models.CharField(max_length=30,verbose_name='کشور')
    city=models.CharField(max_length=30,verbose_name='شهر')
    description=models.TextField(verbose_name='توضیحات')
    experience=models.PositiveIntegerField(verbose_name='تجربه')
    finished=models.PositiveIntegerField(verbose_name='اتمام یافته')
    condition=models.ForeignKey(Condition,on_delete=models.CASCADE,null=True,verbose_name='وضعیت')
    resume=models.FileField(upload_to='pdf_about/%Y/%b',verbose_name='رزومه')
    image=models.ImageField(upload_to='image_about/%Y/%b',verbose_name='عکس')
    favorites=models.ForeignKey(Favorites,on_delete=models.CASCADE,null=True,verbose_name='علایق')
    service=models.ForeignKey(Service,on_delete=models.CASCADE,null=True,verbose_name='خدمات')
    opinions=models.ForeignKey(Opinions,on_delete=models.CASCADE,null=True,verbose_name='دیدگاه مشتریان')
    prices=models.ForeignKey(Prices,on_delete=models.CASCADE,null=True,verbose_name='قیمت ها')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name='درباره'
        verbose_name_plural='درباره من'
