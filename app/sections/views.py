from smtplib import SMTPAuthenticationError

from django.core.mail import EmailMessage
from django.http import Http404
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _


class ConfigIsPresentMixin(object):
    def get(self, request, *args, **kwargs):
        if not getattr(self, 'config', None):
            raise Http404
        return super(ConfigIsPresentMixin, self).get(request, *args, **kwargs)


def contact(request):
    message = _('Ok, thank you')
    try:
        email = EmailMessage('title', 'body', to=['piotrkrych@pnet.eu'])
        email.send()
    except ConnectionRefusedError:
        message = _('Sorry, Connection refused, please try again')
    except SMTPAuthenticationError:
        message = _('Sorry, SMTP Authentication Error, please try again')
    except Exception:
        message = _('Unknown error, please try again')
    return JsonResponse({'message': message.encode('utf-8').decode('utf-8')})
