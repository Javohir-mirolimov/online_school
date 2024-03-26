from django.db import models



class Reader(models.Model):
    user = models.OneToOneField(to='User', verbose_name='Foydalanuvchi')
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
    user = models.OneToOneField(to='User', verbose_name='Foydalanuvchi')
    science = models.ForeignKey(to='Science', verbose_name='Fan', null=True, blank=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(to='Room', null=True, blank=True, verbose_name='xona', on_delete=models.SET_NULL )

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = "O'qituvchi"


class Class(models.Model):
    name = models.CharField(max_length=10, verbose_name='Nomi')
    number = models.IntegerField(verbose_name="O'quvchilar soni")
    room = models.ForeignKey(to='Room', null=True, blank=True, verbose_name='Xona', on_delete=models.SET_NULL)
    science = models.ManyToManyField(to='Class_science', verbose_name='Fanlar',)

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




