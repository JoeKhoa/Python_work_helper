from django.core.mail import send_mail
from django_email_celery.settings import EMAIL_HOST_USER

# # from django.core.mail import send_mail
# # send_mail(
# #     'Subject here',
# #     'Here is the message.',
# #     'from@example.com',
# #     ['to@example.com'],
# #     fail_silently=False,
# )


def send_mail_to(subject, message, receivers):
    send_mail(subject,message,EMAIL_HOST_USER,[receivers],
    fail_silently= False)