from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class contactFormModel(models.Model):
    username = models.CharField(max_length=50, verbose_name='Adınız Soyadınız')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=50, verbose_name='Mail Adresiniz')
    subject = models.CharField(max_length=50, verbose_name='Konu')
    message = models.CharField(max_length=50, verbose_name='Mesajınız')
    
    
    def __str__(self):
        return self.username