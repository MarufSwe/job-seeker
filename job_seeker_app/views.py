import json

from django.contrib.auth import authenticate
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import *
from .helpers import json_body

from .models import *


# Create your views here.

# =========================================Registration================================

# JobSeeker Registration
# http://127.0.0.1:8000/registration
@method_decorator(csrf_exempt, name='dispatch')
class JobSeekerRegistration(View):
    def post(self, request):
        # getting api data
        seeker_form = UserForm(json_body(request))
        if seeker_form.is_valid():
            seeker_form.instance.save()
            return JsonResponse({'message': 'Registration Successful!'}, status=201, safe=False)
        else:
            return JsonResponse({'message': seeker_form.errors}, status=422)


# Login
# http://127.0.0.1:8000/login/
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    # getting api data
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    username = body['username']
    password = body['password']

    # if data available
    if username and password:

        # checking
        authenticated = authenticate(username=username, password=password)

        # if authenticated user
        if authenticated:
            # generating token
            token = generate_token()

            # creating object
            Token.objects.create(user=authenticated, token=token)

            # if succeed
            return JsonResponse({'token': token}, status=200)

        # if not succeed
        else:
            return JsonResponse({'message': 'Login Failed!'}, status=401)

    # if data not available
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)


# Logout
# http://127.0.0.1:8000/logout/
def logout(request):
    # getting token
    token = request.headers['Token']

    # if token available
    if token:
        # matching api token with db token
        matched_token = Token.objects.get(token=token)
        # deleting db token
        matched_token.delete()

        # if succeed
        return JsonResponse({'message': 'Logout Successfully!'}, status=200)

    # if not succeed
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)


# custom token generating
def generate_token():
    import time
    return str(int(time.time()))


# Register JobSeeker List
# http://127.0.0.1:8000/seeker_list
def job_seeker_list(request):
    register_seeker_list = {'register_seeker_list': list(User.objects.values())}
    return JsonResponse(register_seeker_list, safe=False)


# ===========================================Personal Info============================================

# Personal Info List
# http://127.0.0.1:8000/personal_info/
def personal_information(request):
    per_info = {'per_info': list(PersonalInfo.objects.values())}
    return JsonResponse(per_info, safe=False)


# Add PersonalInfo
# http://127.0.0.1:8000/add_per_info/
@csrf_exempt
@require_http_methods(["POST"])
def create_personal_info(request):
    # getting api data
    user_personal_info = UserPersonalInfo(json_body(request))

    # validation
    if user_personal_info.is_valid():
        user_personal_info.instance.save()
        return JsonResponse({'message': 'Personal Info Successfully added '}, status=201, safe=False)
    else:
        return JsonResponse({'message': user_personal_info.errors}, status=422)


# Update Personal Info
# http://127.0.0.1:8000/update_per_info/
@method_decorator(csrf_exempt, name='dispatch')
class UpdatePersonalInfo(View):
    def put(self, request, id=None):

        # catch the editable id (object)
        per_info_id = PersonalInfo.objects.get(id=id)

        # getting api data
        form = UpdateUserInfo(json_body(request), instance=per_info_id)

        # validation
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Personal Info Updated!"}, status=201, safe=False)
        else:
            return JsonResponse({"message": form.errors}, status=404, safe=False)


# Delete PersonalInfo
# http://127.0.0.1:8000/del_per_info
@csrf_exempt
def delete_personal_info(request, id):
    personal_info = get_object_or_404(PersonalInfo, id=id)
    if request.method == "POST":
        personal_info.delete()
        return JsonResponse({'massage': 'Personal Info delete successfully'}, status=204)
    else:
        return JsonResponse({"message": personal_info.errors}, status=422)


# ===============================================Professional Info===============================================


# Professional Info List
# http://127.0.0.1:8000/professional_info/
def professional_information(request):
    pro_info = {'pro_info': list(ProfessionalInfo.objects.values())}
    return JsonResponse(pro_info, safe=False)


# Add ProfessionalInfo
# http://127.0.0.1:8000/add_pro_info/
@csrf_exempt
@require_http_methods(["POST"])
def create_professional_info(request):
    # getting api data
    user_professional_info = UserProfessionalInfo(json_body(request))

    # validation
    if user_professional_info.is_valid():
        user_professional_info.instance.save()
        return JsonResponse({"message": "Professional Info Successfully added"}, status=201, safe=False)
    else:
        return JsonResponse({"message": user_professional_info.errors}, status=422)


# Update Professional Info
# http://127.0.0.1:8000/update_pro_info/
@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfessionalInfo(View):
    def put(self, request, id=id):

        # catch the editable id (object)
        pro_info_id = ProfessionalInfo.objects.get(id=id)

        # getting api data
        form = EditProfessionalInfo(json_body(request), instance=pro_info_id)

        # validation
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Professional Info Updated!"}, status=201, safe=False)
        else:
            return JsonResponse({"message": form.errors}, status=404, safe=False)


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


# Add Degree
# http://127.0.0.1:8000/add_degree/
@csrf_exempt
@require_http_methods(["POST"])
def create_degree(request):
    # getting api data
    user_degree = UserDegree(json_body(request))

    # validation
    if user_degree.is_valid():
        user_degree.instance.save()
        return JsonResponse({'message': 'Degree added successfully'}, status=201, safe=False)
    else:
        return JsonResponse({'message': user_degree.errors}, status=422)


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


# ===============================================Academic Info===============================================

# AcademicInfo List
# http://127.0.0.1:8000/academic_info
def academic_info_list(request):
    academic_info = {'academic_info': list(AcademicInfo.objects.values())}
    return JsonResponse(academic_info, safe=False)


# Add AcademicInfo
# http://127.0.0.1:8000/add_academic_info/
@csrf_exempt
@require_http_methods(["POST"])
def create_academic_info(request):
    # get api data
    user_academic_info = UserAcademicInfo(json_body(request))

    # validation
    if user_academic_info.is_valid():
        user_academic_info.instance.save()
        return JsonResponse({'message': 'Academic Info Added Successfully'}, status=201, safe=False)
    else:
        return JsonResponse({'message': user_academic_info.errors}, status=422)


# Update Academic Info
# http://127.0.0.1:8000/update_academic/
@method_decorator(csrf_exempt, name='dispatch')
class UpdateAcademicInfo(View):
    def put(self, request, id=id):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            result = body['result']
            year_from = body['year_from']
            year_to = body['year_to']
            institute_name = body['institute_name']

            exist_academic = get_object_or_404(AcademicInfo, id=id)

            exist_academic.result = result
            exist_academic.save()

            exist_academic.year_from = year_from
            exist_academic.save()

            exist_academic.year_to = year_to
            exist_academic.save()

            exist_academic.institute_name = institute_name
            exist_academic.save()

            return JsonResponse({"message": "updated"}, status=201, safe=False)

        except AcademicInfo.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


# Delete Academic info
# http://127.0.0.1:8000/del_academic
@csrf_exempt
def delete_academic_info(request, id):
    academic = get_object_or_404(AcademicInfo, id=id)
    if request.method == "POST":
        academic.delete()
    return JsonResponse({'massage': 'delete successfully'}, status=204, safe=False)
