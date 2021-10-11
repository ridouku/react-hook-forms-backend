from django.db import models


class Person(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10)
    identification = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10, default='')


class Pet(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    owner = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
