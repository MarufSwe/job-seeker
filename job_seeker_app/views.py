import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import *


# Create your views here.

# ===========================================Personal Info============================================

# Personal Info List
# http://127.0.0.1:8000/personal_info/
def personal_information(request):
    per_info = {'per_info': list(PersonalInfo.objects.values())}
    return JsonResponse(per_info, safe=False)


# Professional Info List
# http://127.0.0.1:8000/professional_info/
def professional_information(request):
    pro_info = {'pro_info': list(ProfessionalInfo.objects.values())}
    return JsonResponse(pro_info, safe=False)


# Add PersonalInfo
# http://127.0.0.1:8000/add_per_info/
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


# Update Personal Info
# http://127.0.0.1:8000/update_per_info/
@method_decorator(csrf_exempt, name='dispatch')
class UpdatePersonalInfo(View):
    def put(self, request, id=id):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            first_name = body['first_name']
            last_name = body['last_name']
            mobile = body['mobile']
            email = body['email']
            father_name = body['father_name']
            mother_name = body['mother_name']
            gender = body['gender']
            religion = body['religion']
            nid = body['nid']
            dob = body['dob']

            exist_per_info = get_object_or_404(PersonalInfo, id=id)

            exist_per_info.first_name = first_name
            exist_per_info.save()

            exist_per_info.last_name = last_name
            exist_per_info.save()

            exist_per_info.mobile = mobile
            exist_per_info.save()

            exist_per_info.email = email
            exist_per_info.save()

            exist_per_info.father_name = father_name
            exist_per_info.save()

            exist_per_info.mother_name = mother_name
            exist_per_info.save()

            exist_per_info.gender = gender
            exist_per_info.save()

            exist_per_info.religion = religion
            exist_per_info.save()

            exist_per_info.nid = nid
            exist_per_info.save()

            exist_per_info.dob = dob
            exist_per_info.save()

            return JsonResponse({"message": "updated"}, status=201, safe=False)

        except ProfessionalInfo.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


# Delete PersonalInfo
# http://127.0.0.1:8000/del_per_info
@csrf_exempt
def delete_personal_info(request, id):
    personal_info = get_object_or_404(PersonalInfo, id=id)
    if request.method == "POST":
        personal_info.delete()
    return JsonResponse({'massage': 'delete successfully'}, status=204)


# ===============================================Professional Info===============================================

# Add ProfessionalInfo
# http://127.0.0.1:8000/add_pro_info/
@csrf_exempt
@require_http_methods(["POST"])
def create_professional_info(request):
    import json
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    print(body_data)

    company_name = body_data['company_name']
    company_type = body_data['company_type']
    employee_id = body_data['employee_id']
    designation = body_data['designation']
    department = body_data['department']
    responsibilities = body_data['responsibilities']
    company_location = body_data['company_location']
    employment_period = body_data['employment_period']
    user = body_data['user']
    print(user)

    custom_user = CustomUser.objects.get(id=user)
    print(custom_user)

    data = ProfessionalInfo.objects.create(
        company_name=company_name,
        company_type=company_type,
        employee_id=employee_id,
        designation=designation,
        department=department,
        responsibilities=responsibilities,
        company_location=company_location,
        employment_period=employment_period,
        user=custom_user
    )
    return JsonResponse(str(data), safe=False)


# Update Professional Info
# @csrf_exempt
# @require_http_methods(["POST"])
# def update_professional_info(request, id=None):
#     # receiving API data
#     # received_id = request.POST.get('id')
#     company_name = request.POST.get('company_name')
# company_type = request.POST.get('company_type')
# employee_id = request.POST.get('employee_id')
# designation = request.POST.get('designation')
# department = request.POST.get('department')
# responsibilities = request.POST.get('responsibilities')
# company_location = request.POST.get('company_location')
# employment_period = request.POST.get('employment_period')

# if received_id:
# exist_pro_info = ProfessionalInfo.objects.get(id=id)
# updating object
# exist_pro_info.company_name = company_name
# exist_pro_info.save()
# exist_pro_info.company_type = company_type
# exist_pro_info.save()
# exist_pro_info.employee_id = employee_id
# exist_pro_info.save()
# exist_pro_info.designation = designation
# exist_pro_info.save()
# exist_pro_info.department = department
# exist_pro_info.save()
# exist_pro_info.responsibilities = responsibilities
# exist_pro_info.save()
# exist_pro_info.company_location = company_location
# exist_pro_info.save()
# exist_pro_info.employment_period = employment_period
# exist_pro_info.save()
# print(existing_post.title, existing_post.body)
# return JsonResponse({'message': exist_pro_info}, status=200)

# Update Professional Info
# http://127.0.0.1:8000/update_pro_info/
@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfessionalInfo(View):
    def put(self, request, id=id):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            company_name = body['company_name']
            company_type = body['company_type']
            employee_id = body['employee_id']
            designation = body['designation']
            department = body['department']
            responsibilities = body['responsibilities']
            company_location = body['company_location']
            employment_period = body['employment_period']

            exist_pro_info = get_object_or_404(ProfessionalInfo, id=id)

            exist_pro_info.company_name = company_name
            exist_pro_info.save()

            exist_pro_info.company_type = company_type
            exist_pro_info.save()

            exist_pro_info.employee_id = employee_id
            exist_pro_info.save()

            exist_pro_info.designation = designation
            exist_pro_info.save()

            exist_pro_info.department = department
            exist_pro_info.save()

            exist_pro_info.responsibilities = responsibilities
            exist_pro_info.save()

            exist_pro_info.company_location = company_location
            exist_pro_info.save()

            exist_pro_info.employment_period = employment_period
            exist_pro_info.save()

            return JsonResponse({"message": "updated"}, status=201, safe=False)

        except ProfessionalInfo.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


# Delete Professional Info
# http://127.0.0.1:8000/del_pro_info
@csrf_exempt
def delete_professional_info(request, id):
    professional_info = get_object_or_404(ProfessionalInfo, id=id)
    if request.method == "POST":
        professional_info.delete()
    return JsonResponse({'massage': 'delete successfully'}, status=204)


# ===============================================Degree===============================================

# Degree Name List
# http://127.0.0.1:8000/degree
def degree_name(request):
    degree = {'degree': list(Degree.objects.values())}
    return JsonResponse(degree, safe=False)


# Add PersonalInfo
# http://127.0.0.1:8000/add_degree/
@csrf_exempt
@require_http_methods(["POST"])
def create_degree(request):
    import json
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    degree_name = body_data['degree_name']

    custom_user = Degree.objects.get()
    print(custom_user)

    data = Degree.objects.create(
        degree_name=degree_name,
    )
    return JsonResponse(str(data), safe=False)


# Update Degree
# http://127.0.0.1:8000/update_degree/
@method_decorator(csrf_exempt, name='dispatch')
class UpdateDegree(View):
    def put(self, request, id=id):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            degree_name = body['degree_name']

            exist_degree = get_object_or_404(Degree, id=id)

            exist_degree.degree_name = degree_name
            exist_degree.save()

            return JsonResponse({"message": "updated"}, status=201, safe=False)

        except Degree.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


# Delete Degree
# http://127.0.0.1:8000/del_degree
@csrf_exempt
def delete_degree(request, id):
    degree = get_object_or_404(Degree, id=id)
    if request.method == "POST":
        degree.delete()
    return JsonResponse({'massage': 'delete successfully'}, status=204)
