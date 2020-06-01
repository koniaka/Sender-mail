from django.db import models
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import time
import threading


class Email(models.Model):
    date = models.DateTimeField('Дата создания', auto_now_add=True, editable=True)
    interval = models.PositiveIntegerField('Отправить через,с')
    subject = models.CharField('Тема письма', max_length=50)
    message = models.TextField('Сообщение', max_length=500)
    send_to = models.EmailField('Получатель')

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        threads = []

        def mail_send(subject, message, email, interval):
            time.sleep(interval)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently=False)

        t = threading.Thread(target=mail_send, args=(self.subject, self.message, self.send_to, self.interval))
        threads.append(t)
        t.start()

