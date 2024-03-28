from django.db import models
from account.models import User

class Reader(models.Model):
    user = models.OneToOneField(User, verbose_name="Foydalanuvchi", on_delete=models.CASCADE)
    teachers = models.ManyToManyField('Teacher', verbose_name="O'qituvchi")
    schedule = models.FileField(verbose_name="Dars Jadvali", null=True, blank=True)
    grades = models.FileField(verbose_name="Dars Baholari", null=True, blank=True)
    class_field = models.ForeignKey('Class', verbose_name="Sinfi", null=True, blank=True, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=(
        (1, 'Yaxshi'),
        (2, 'Ortacha'),
        (3, 'Yomon')
    ), default=2)

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"

class Teacher(models.Model):
    user = models.OneToOneField(User, verbose_name="Foydalanuvchi", on_delete=models.CASCADE)
    sciences = models.ManyToManyField('Science', verbose_name="Fanlar", blank=True)
    room = models.ForeignKey('Room', verbose_name="Xona", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"

class Class(models.Model):
    name = models.CharField(max_length=10, verbose_name="Nomi")
    number_of_students = models.IntegerField(verbose_name="O'quvchilar Soni")
    room = models.ForeignKey('Room', verbose_name="Xona", null=True, blank=True, on_delete=models.SET_NULL)
    sciences = models.ManyToManyField('Science', verbose_name="Fanlar", blank=True)
    status = models.IntegerField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
    ))

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinf"

class Room(models.Model):
    number = models.CharField(max_length=10, verbose_name="Raqam")

    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"

class Science(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

class ClassScience(models.Model):
    class_field = models.ForeignKey('Class', verbose_name="Sinf", on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey('Teacher', verbose_name="O'qituvchi", on_delete=models.SET_NULL, null=True, blank=True)
    science = models.ForeignKey('Science', verbose_name="Fan", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Sinf Fan"
        verbose_name_plural = "Sinf Fanlari"

class Test(models.Model):
    class_field = models.IntegerField(verbose_name="Sinf")
    science = models.ForeignKey('Science', verbose_name="Fan", on_delete=models.CASCADE)
    question = models.TextField(verbose_name="Savol")
    option_a = models.CharField(max_length=255, verbose_name="Variant A")
    option_b = models.CharField(max_length=255, verbose_name="Variant B")
    option_c = models.CharField(max_length=255, verbose_name="Variant C")
    option_d = models.CharField(max_length=255, verbose_name="Variant D")
    answer = models.CharField(max_length=1, choices=(
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D')
    ), verbose_name="To'g'ri javob")

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
