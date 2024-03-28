from django.db import models
from account.models import User


class Reader(models.Model):
    user = models.OneToOneField(to='User', verbose_name='Foydalanuvchi', on_delete=models.CASCADE)
    teachers = models.ManyToManyField(to='Teacher', verbose_name="O'qituvchsi")
    schedule = models.FileField(verbose_name='dars jadvali', null=True, blank=True)
    grades = models.FileField(verbose_name='dars baholari', null=True, blank=True)
    clas = models.ForeignKey(to='Class', verbose_name='Sinfi', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=(
        (1, 'good'),
        (2, 'medium'),
        (3, 'bad')
    ), default=2)

    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = "O'quvchi"


class Teacher(models.Model):
    user = models.OneToOneField(to='User', verbose_name='Foydalanuvchi', on_delete=models.CASCADE)
    science = models.ManyToManyField(to='Science', verbose_name='Fan', blank=True,)
    room = models.ForeignKey(to='Room', null=True, blank=True, verbose_name='xona', on_delete=models.SET_NULL )

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = "O'qituvchi"


class Class(models.Model):
    name = models.CharField(max_length=10, verbose_name='Nomi')
    number = models.IntegerField(verbose_name="O'quvchilar soni")
    room = models.ForeignKey(to='Room', null=True, blank=True, verbose_name='Xona', on_delete=models.SET_NULL)
    science = models.ManyToManyField(to='Class_science', verbose_name='Fanlar', blank=True)
    status = models.IntegerField(choices=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8,8),
        (9, 9),
        (10, 10),
        (11, 11),
    ))

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = "Sinf"


class Room(models.Model):
    number = models.CharField(max_length=10, verbose_name='Raqam')

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Xona'


class Class_science(models.Model):
    science = models.ForeignKey(to='Science', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Fan')
    teacher = models.ForeignKey(to='Teacher', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="O'qituvchi")

    class Meta:
        verbose_name = 'Class_science'
        verbose_name_plural = 'Sinf fani'


class Science(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Science'
        verbose_name_plural = 'Fan'


class Test(models.Model):
    clas = models.IntegerField(verbose_name='Sinf')
    science = models.ForeignKey(to='Science', on_delete=models.CASCADE, verbose_name='Fan')
    question = models.TextField( verbose_name='Savol')
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)
    answer = models.CharField(max_length=1, choices=(
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd')
    ))




