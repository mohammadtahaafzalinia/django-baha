import uuid

from django.db import models
# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=30,verbose_name='نام')
    en_name=models.CharField(max_length=50,null=True,verbose_name='نام به انگلیسی')
    logo=models.FileField(upload_to='logo/%Y/%b')
    language=models.BooleanField(default=False,verbose_name='زبان')
    language_code=models.UUIDField(default=uuid.uuid4,editable=False,verbose_name='کدزبان')
    twitter=models.URLField(blank=True,verbose_name='ادرس اکانت توییتر')
    youtube=models.URLField(blank=True,verbose_name='ادرس اکانت یوتیوب')
    facebook=models.URLField(blank=True,verbose_name='ادرس اکانت فیسبوک')
    instagram=models.URLField(blank=True,verbose_name='ادرس اکانت اینستاگرام')


    class Meta:
        verbose_name = 'خانه'
        verbose_name_plural = 'تنظیمات صغحه خانه'

    def __str__(self):
        return self.name
