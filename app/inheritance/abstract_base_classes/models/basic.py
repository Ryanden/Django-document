from django.db import models

# Create your models here.

__all__ = (
    'CommonInfo1',
    'CommonInfo2',
    'User',
    'Student'
)


class CommonInfo1(models.Model):
    name = models.CharField(max_length=50, default=None)

    class Meta:
        abstract = True
        ordering = ['-name']


class CommonInfo2(CommonInfo1):
    age = models.IntegerField(default=0)

    class Meta(CommonInfo1.Meta):
        abstract = True
        verbose_name = 'CommonInfo2'


class User(CommonInfo1):
    username = models.CharField(max_length=50, default=None)


class Student(CommonInfo2):
    cls = models.CharField(max_length=50)


