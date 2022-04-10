# Generated by Django 3.1.7 on 2022-04-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage1', '0008_auto_20220330_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactFormModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Name Surname')),
                ('phone', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, verbose_name='Your Mail Adress')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('message', models.CharField(max_length=50, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='referansi2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1_Image', models.ImageField(blank=True, null=True, upload_to='refer')),
                ('title2_adres', models.CharField(blank=True, max_length=100, null=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='staticAboutModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1_Image', models.ImageField(blank=True, null=True, upload_to='about')),
                ('title2', models.CharField(max_length=100, verbose_name='Sağ Başlık')),
                ('content', models.CharField(max_length=1300, verbose_name='İçerik')),
                ('content2', models.CharField(max_length=1300, verbose_name='İçerik2')),
            ],
        ),
        migrations.CreateModel(
            name='subFormModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Your Mail Adress')),
            ],
        ),
    ]