# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save, sender=DemoRequest)
def send_demo_request_email(sender, instance, created, **kwargs):
    if not created:
        return
    subject = "📞 New Demo Request Received"
    message = (
        f"Name:    {instance.full_name}\n"
        f"Email:   {instance.email}\n"
        f"Company: {instance.company or '—'}\n"
        f"Phone:   {instance.phone or '—'}\n\n"
        f"Date/Time: {instance.datetime or '—'}\n\n"
        f"Message:\n{instance.message or '—'}\n\n"
        f"Requested at: {instance.created_at:%Y-%m-%d %H:%M}"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ["marvinavi24@gmail.com"],
        fail_silently=False,
    )
