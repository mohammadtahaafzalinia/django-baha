from django.db import models
from jalali_date import *
# Create your models here.
class Resume_educational(models.Model):
    section=models.CharField(max_length=30,verbose_name='مقطع تحصیلی')
    field_study=models.CharField(max_length=50,verbose_name='رشته تحصیلی')
    start_time=models.DateField(verbose_name='زمان شروع')
    end_time=models.DateField(verbose_name='زمان اتمام')
    description=models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = 'سوابق تحصیلی'

    def __str__(self):
        return self.section

    def get_jalali_start_time(self):
        return date2jalali(self.start_time).strftime('%Y')

    def get_jalali_end_time(self):
        return date2jalali(self.end_time).strftime('%Y')


class Resume_model(models.Model):
    work = models.CharField(max_length=30, verbose_name='کار')
    company = models.CharField(max_length=50, verbose_name='شرکت')
    start_time = models.DateField(verbose_name='زمان شروع')
    end_time = models.DateField(verbose_name='زمان اتمام')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سوابق کاری'

    def __str__(self):
        return self.work

    def get_jalali_start_time(self):
        return date2jalali(self.start_time).strftime('%Y')

    def get_jalali_end_time(self):
        return date2jalali(self.end_time).strftime('%Y')


class Skills(models.Model):
     skill_name=models.CharField(max_length=30,verbose_name='نام مهارت')
     percent=models.IntegerField(default=100,verbose_name='درصد توانایی')
     type_name=(
         ('circle','دایره'),
         ('linear','خطی')
     )
     type_skill=models.CharField(max_length=10,choices=type_name,verbose_name='نوع نمودار')
     color=models.CharField(max_length=10,default='#fff',verbose_name='رنگ')

     class Meta:
         verbose_name = 'مهارت'
         verbose_name_plural = 'مهارت ها'

     def __str__(self):
         return self.skill_name


class Work_process(models.Model):
    number_work=models.IntegerField(verbose_name='شماره مرحله')
    title=models.CharField(max_length=30,verbose_name='عنوان')
    description=models.CharField(max_length=150,verbose_name='توضیحات کوتاه')

    class Meta:
        verbose_name = 'پروسه کار'
        verbose_name_plural = 'پروسه کاری'


    def __str__(self):
        return self.title
