from django.http import JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def personal_information(request):
    per_info = {'per_info': list(PersonalInfo.objects.values())}
    return JsonResponse(per_info, safe=False)


def professional_information(request):
    pro_info = {'pro_info': list(ProfessionalInfo.objects.values())}
    return JsonResponse(pro_info, safe=False)