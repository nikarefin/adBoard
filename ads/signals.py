from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Response


@receiver(post_save, sender=Response)
def response_created(instance, created, **kwargs):
    if not created:
        return

    ad_author_email = instance.ad.author.email

    subject = f'Новый отклик на ваше объявление {instance.ad.title}'

    text_content = (
        f'Текст отклика: {instance.text}\n'
    )

    msg = EmailMultiAlternatives(subject, text_content, None, [ad_author_email])
    msg.send()


@receiver(post_save, sender=Response)
def response_accepted(instance, **kwargs):
    user_email = instance.author.email

    if instance.status == 'accepted':
        subject = f'Ваш отклик на объявление {instance.ad.title} принят'
        text_content = f'Ваш отклик на объявление был принят. Отклик: {instance.text}'
    else:
        return

    msg = EmailMultiAlternatives(subject, text_content, None, [user_email])
    msg.send()
