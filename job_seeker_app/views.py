import json

from django.contrib.auth import authenticate
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
    import json
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
    def put(self, request, id=id):
        try:
            # getting api data
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

    custom_user = User.objects.get(id=user)
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


# Add Degree
# http://127.0.0.1:8000/add_degree/
@csrf_exempt
@require_http_methods(["POST"])
def create_degree(request):
    import json
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    degree_name = body_data['degree_name']
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
    import json
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    result = body_data['result']
    year_from = body_data['year_from']
    year_to = body_data['year_to']
    institute_name = body_data['institute_name']
    degree = body_data['degree']
    board = body_data['board']
    user = body_data['user']

    custom_user = User.objects.get(id=user)
    print(custom_user)
    foreign_degree = Degree.objects.get(id=degree)
    print(degree)
    board_name = Board.objects.get(id=board)
    # print(board_name)

    data = AcademicInfo.objects.create(
        result=result,
        year_from=year_from,
        year_to=year_to,
        institute_name=institute_name,
        degree=foreign_degree,
        board=board_name,
        user=custom_user
    )
    return JsonResponse(str(data), safe=False)


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
