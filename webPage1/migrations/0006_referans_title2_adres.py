# Generated by Django 3.1.7 on 2022-03-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage1', '0005_referans'),
    ]

    operations = [
        migrations.AddField(
            model_name='referans',
            name='title2_adres',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='url'),
        ),
    ]