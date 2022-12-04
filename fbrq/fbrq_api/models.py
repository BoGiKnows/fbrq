from django.db import models
import datetime

now = datetime.datetime.now()
now_plus = now + datetime.timedelta(hours=1)
print(now)
print(now_plus)


class Client(models.Model):
    phone = models.CharField(max_length=12)
    phone_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=150)
    timezone = models.CharField(max_length=3)


class Tags(models.Model):
    name = models.CharField(max_length=150)


class Codes(models.Model):
    name = models.CharField(max_length=3)


class MailDis(models.Model):
    start_time = models.DateTimeField()
    mes = models.TextField()
    tags = models.ManyToManyField(Tags)
    phone_code = models.ManyToManyField(Codes)
    end_time = models.DateTimeField()


class Message(models.Model):
    CHOICES = (
        ('awaiting', 'Ожидаем отсылку'),
        ('sending', 'Отсылается...'),
        ('stop', 'Отсылка завершена')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=CHOICES)
    maildis_id = models.ForeignKey(MailDis, on_delete=models.PROTECT)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
