from django.db import models

from users.models import CustomUser


# Create your models here.

class MailingRecipient(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)

    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', help_text='Укажите владельца продукта',
                              on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.full_name} {self.email}'


class Message(models.Model):
    theme = models.CharField(max_length=100)
    message = models.TextField()

    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', help_text='Укажите владельца продукта',
                              on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.theme}'


class Distribution(models.Model):
    STATUS_CHOICES = (
        ('Completed', 'Завершена'),
        ('Created', 'Создана'),
        ('Launched', 'Запущена'),
    )
    first_sending = models.DateTimeField(auto_now_add=True)
    last_sending = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(MailingRecipient)

    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', help_text='Укажите владельца продукта',
                              on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.message}'


class AttemptToSend(models.Model):
    STATUS_CHOICES = (
        ('Successfully', 'Успешно'),
        ('Not successful', 'Не успешно'),
    )
    date_attempt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    response = models.TextField()
    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE)
