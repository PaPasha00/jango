from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=130)
    task = models.TextField('Описание', max_length=30)

    def __str__(self):
        return self.title

class RegisterUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тренировку'
        verbose_name_plural = 'Тренировки'