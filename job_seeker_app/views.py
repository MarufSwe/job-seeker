from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import *

# Create your views here.


# Personal Info List
def personal_information(request):
    per_info = {'per_info': list(PersonalInfo.objects.values())}
    return JsonResponse(per_info, safe=False)


# Professional Info List
def professional_information(request):
    pro_info = {'pro_info': list(ProfessionalInfo.objects.values())}
    return JsonResponse(pro_info, safe=False)


# Add PersonalInf
@csrf_exempt
@require_http_methods(["POST"])
def create_personal_info(request):
    import json
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    print(body_data)

    first_name = body_data['first_name']
    last_name = body_data['last_name']
    mobile = body_data['mobile']
    email = body_data['email']
    father_name = body_data['father_name']
    mother_name = body_data['mother_name']
    gender = body_data['gender']
    religion = body_data['religion']
    nid = body_data['nid']
    dob = body_data['dob']
    user = body_data['user']
    print(user)

    custom_user = CustomUser.objects.get(id=user)
    print(custom_user)

    data = PersonalInfo.objects.create(
        first_name=first_name,
        last_name=last_name,
        mobile=mobile,
        email=email,
        father_name=father_name,
        mother_name=mother_name,
        gender=gender,
        religion=religion,
        nid=nid,
        dob=dob,
        user=custom_user
    )
    return JsonResponse(str(data), safe=False)


# Delete PersonalInf
@csrf_exempt
def delete_professional_info(request, id):
    personal_info = get_object_or_404(PersonalInfo, id=id)
    if request.method == "POST":
        personal_info.delete()
    return JsonResponse({'massage': 'delete successfully'}, status=204)
