from django.db import models
# Create your models here.
class ContactUs(models.Model):
    phone=models.CharField(max_length=15,default='+98',verbose_name='تلفن')
    address=models.CharField(max_length=150,verbose_name='ادرس')
    email=models.EmailField(verbose_name='ایمیل')

    class Meta:
        verbose_name = 'مشخصات'
        verbose_name_plural = 'مشخصات'

    def __str__(self):
        return self.email


class Contact(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام')
    email_contact=models.EmailField(verbose_name='ایمیل')
    text=models.TextField(verbose_name='پیام شما')
    created_date = models.DateField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    response = models.TextField(verbose_name='پاسخ',null=True)
    read_by_admin = models.BooleanField(editable=False,default=False,blank=True,verbose_name='توسط ادمین خوانده شد' , null=True)
    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.name

