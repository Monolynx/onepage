from django.http import Http404


class ConfigIsPresentMixin(object):
    def get(self, request, *args, **kwargs):
        if not getattr(self, 'config', None):
            raise Http404
        return super(ConfigIsPresentMixin, self).get(request, *args, **kwargs)
