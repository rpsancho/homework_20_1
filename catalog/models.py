from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(null=True, verbose_name='превью')
    category = models.ForeignKey(Category, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    last_change_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
