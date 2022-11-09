from django.core.mail import EmailMultiAlternatives


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMultiAlternatives(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.content_subtype = 'html'
        email.attach_alternative(data['email_body'], "text/html")
        email.mixed_subtype = 'related'
        email.send()