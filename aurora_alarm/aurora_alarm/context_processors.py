from django.conf import settings


def pass_global_variables(request):
    global_variables = {
        'API_URL': settings.API_URL
    }

    return global_variables