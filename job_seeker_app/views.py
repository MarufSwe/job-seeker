from django.http import JsonResponse

from .models import Personals


def api_data(request):
    data = {
        'division': list(Personals.objects.values()),

    }
    return JsonResponse(data, status=200, safe=False)
