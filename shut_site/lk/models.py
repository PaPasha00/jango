from django.db import models

class Articles(models.Model):
    title = models.CharField('ФИО', max_length=50)
    date = models.DateField('Дата тренировки')
    time = models.TimeField('Время тренировки')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тренировку'
        verbose_name_plural = 'Тренировки'