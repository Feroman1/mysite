from django.db import models

class mail(models.Model):
    email = models.CharField('E-mail', max_length=35)
    number = models.CharField('Номер телефона', max_length=15)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'letter'
        verbose_name_plural = 'letters'
# Create your models here.
