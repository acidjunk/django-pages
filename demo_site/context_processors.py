from django.template import Context
from django.template import RequestContext
# from __future__ import unicode_literals
from django.conf import settings
from django.middleware.csrf import get_token
from django.utils.encoding import smart_text
from django.utils.functional import SimpleLazyObject, lazy

# view code here...
# c = Context({'some_var': 'some_value', 'some_other_var': 'some_other_value'})


def media_url(request):
    from django.conf import settings
    return {'media_url': settings.MEDIA_URL}


# def media_url(request):
    # from django.conf import settings

    # return render_to_response("my_app/my_template.html",{'some_var': 'foo'}, context_instance=RequestContext(request))


def csrf(request):
    def _get_val():
        token = get_token(request)
        if token is None:
            # In order to be able to provide debugging info in the
            # case of misconfiguration, we use a sentinel value
            # instead of returning an empty dict.
            return 'NOTPROVIDED'
        else:
            return smart_text(token)

    return {'csrf_token': SimpleLazyObject(_get_val)}


def debug(request):
    context_extras = {}
    if settings.DEBUG and request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
        context_extras['debug'] = True
        from django.db import connection
        context_extras['sql_queries'] = lazy(lambda: connection.queries, list)
    return context_extras



def i18n(request):
    from django.utils import translation
    context_extras = {}
    context_extras['LANGUAGES'] = settings.LANGUAGES
    context_extras['LANGUAGE_CODE'] = translation.get_language()
    context_extras['LANGUAGE_BIDI'] = translation.get_language_bidi()

    return context_extras


def tz(request):
    from django.utils import timezone

    return {'TIME_ZONE': timezone.get_current_timezone_name()}


def static(request):
    return {'STATIC_URL': settings.STATIC_URL}


def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}


def request(request):
    return {'request': request}