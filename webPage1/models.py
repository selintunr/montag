from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class contactFormModel(models.Model):
    username = models.CharField(max_length=50, verbose_name='Adınız Soyadınız')
    phone = models.CharField(max_length=50, null=False, blank=False, unique=True)
    email = models.CharField(max_length=50, verbose_name='Mail Adresiniz')
    subject = models.CharField(max_length=50, verbose_name='Konu')
    message = models.CharField(max_length=50, verbose_name='Mesajınız')
    
    def __str__(self):
        return self.username


class subFormModel(models.Model):
    email = models.CharField(max_length=50, verbose_name='Mail Adresiniz')
    
    def __str__(self):
        return self.email


class staticAboutModel(models.Model):
    title1_Image = models.ImageField(null=True, blank=True, upload_to='about')
    title2 = models.CharField(max_length=100, verbose_name='Sağ Başlık')
    content = models.CharField(max_length=1300, verbose_name='İçerik')
    content2 = models.CharField(max_length=1300, verbose_name='İçerik2')
    
    def __str__(self):
        return self.title2



class referansi(models.Model):
    title1_Image = models.ImageField(null=True, blank=True, upload_to='refer')
    link = models.URLField(max_length = 200, null=True)
   
    



    ###########################################

class contactFormModel2(models.Model):
    username = models.CharField(max_length=50, verbose_name='Name Surname')
    phone = models.CharField(max_length=50, null=False, blank=False, unique=True)
    email = models.CharField(max_length=50, verbose_name='Your Mail Adress')
    subject = models.CharField(max_length=50, verbose_name='Subject')
    message = models.CharField(max_length=50, verbose_name='Message')
    
    def __str__(self):
        return self.username


class subFormModel2(models.Model):
    email = models.CharField(max_length=50, verbose_name='Your Mail Adress')
    
    def __str__(self):
        return self.email


class staticAboutModel2(models.Model):
    title1_Image = models.ImageField(null=True, blank=True, upload_to='about2')
    title2 = models.CharField(max_length=100, verbose_name='Sağ Başlık')
    content = models.CharField(max_length=1300, verbose_name='İçerik')
    content2 = models.CharField(max_length=1300, verbose_name='İçerik2')
    
    def __str__(self):
        return self.title2



class referansi2(models.Model):
    title1_Image = models.ImageField(null=True, blank=True, upload_to='refer')
    title2_adres = models.CharField(null=True, blank=True , max_length=100, verbose_name='url')
   