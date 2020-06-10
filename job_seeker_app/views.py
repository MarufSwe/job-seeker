import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import (
    AcademicForm,
    ProfessionalsForm,
    PersonalsForm,
    DegreeForm,
    EducationLevelForm,
)

from .models import (
    Personals,
    Professionals,
    Academics,
    EducationLevel,
    Degree,
    Token,
)


def getModelData(self, request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body

# EducationLevel API CR
# EducationLevel read(get),create(post):http://127.0.0.1:8000/seeker/api/education-level/
@method_decorator(csrf_exempt, name='dispatch')
class ViewEducationLevel(View):
    def get(self, request):
        data = {
            "education_list": list(EducationLevel.objects.values())
        }
        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def post(self, request):
        body = getModelData(self, request)
        form = EducationLevelForm(body)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'EducationLevelForm Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

# Degree API CRUD
# Degree Details(get),create(post):http://127.0.0.1:8000/seeker/api/degree/
# Degree Update(update),Delete(delete):http://127.0.0.1:8000/seeker/api/degree/
@method_decorator(csrf_exempt, name='dispatch')
class ViewDegree(View):
    def get(self, request):
        data = {
            "degree_list": list(Degree.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def post(self, request):
        body = getModelData(self, request)
        form = DegreeForm(body)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Degree Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def put(self, request, id=None):
        try:
            body = getModelData(self, request)
            degree_id = Degree.objects.get(id=id)
            form = DegreeForm(body, instance=degree_id)

            if form.is_valid():
                form.save()

            return JsonResponse({"message": "Updated!"}, status=201, safe=False)

        except Professionals.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)

    def delete(self, request, id):
        degree = get_object_or_404(Degree, id=id)
        if degree:
            degree.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


# Professionals API CRUD
# Profession Details(get),Create(post):http://127.0.0.1:8000/seeker/api/professionals/
# Profession Update(put),Delete(delete):http://127.0.0.1:8000/seeker/api/professionals/id
@method_decorator(csrf_exempt, name='dispatch')
class ViewProfessionals(View):
    def get(self, request):
        data = {
            "professionals_list": list(Professionals.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def post(self, request):
        body = getModelData(self, request)
        form = ProfessionalsForm(body)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Professional Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def put(self, request, id=None):
        try:
            body = getModelData(self, request)
            professional_update_id = Professionals.objects.get(id=id)
            form = ProfessionalsForm(body, instance=professional_update_id)

            if form.is_valid():
                form.save()
            return JsonResponse({"message": "Updated!"}, status=201, safe=False)

        except Professionals.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)

    def delete(self, request, id):
        professionals = get_object_or_404(Professionals, id=id)
        if professionals:
            professionals.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


# Personals API CRUD
# Personal Details(get), Create personal (post) :http://127.0.0.1:8000/seeker/api/personals/
# Personal Update(update), Delete personal (delete) :http://127.0.0.1:8000/seeker/api/personals/id
@method_decorator(csrf_exempt, name='dispatch')
class ViewPersonals(View):
    def get(self, request):
        data = {
            "personals_list": list(Personals.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def post(self, request):
        body = getModelData(self, request)
        form = PersonalsForm(body)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Personal Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def put(self, request, id=None):
        try:
            body = getModelData(self, request)

            personal_id = Personals.objects.get(id=id)

            form = PersonalsForm(body, instance=personal_id)

            if form.is_valid():
                form.save()
            return JsonResponse({"message": "Updated!"}, status=201, safe=False)

        except Personals.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)

    def delete(self, request, id=None):
        personals = get_object_or_404(Personals, id=id)

        if personals:
            personals.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


# Academics CRUD
# Academics Details(get), create(post):http://127.0.0.1:8000/seeker/api/academics/
# Academics Update(update), delete(delete):http://127.0.0.1:8000/seeker/api/academics/id

@method_decorator(csrf_exempt, name='dispatch')
class ViewAcademics(View):
    def get(self, request):
        data = {
            "academics_list": list(Academics.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)

    def post(self, request):
        body = getModelData(self, request)
        form = AcademicForm(body)

        if form.is_valid():
            form.save()
            return JsonResponse({'data': 'Academics Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"errors": form.errors.as_json()}, status=422)

    def put(self, request, id=id):
        try:
            body = getModelData(self, request)
            academic_id = Academics.objects.get(id=id)
            form = AcademicForm(body, instance=academic_id)

            if form.is_valid():
                form.save()
                return JsonResponse({'data': 'Update Academic info !'}, status=201, safe=False)
        except Academics.DoesNotExist as e:
            return JsonResponse({"errors": form.errors.as_json()}, status=404, safe=False)

    def delete(self, request, id=None):
        academics = get_object_or_404(Academics, id=id)
        if academics:
            academics.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def sign_up(request):
    # getting api data
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    username = body['username']
    email = body['email']
    password = body['password']
    first_name = body['first_name']
    last_name = body['last_name']

    # if data available
    if username and email and password and first_name and last_name:
        # user creation
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # modifying data to json format
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        # return api response
        return JsonResponse(user_data, status=201)

    # if data not available
    else:
        return JsonResponse({'message': 'Signup Failed!'}, status=404)


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


@csrf_exempt
@require_http_methods(["POST"])
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

# from .forms import UserForm


# login
# logout
# Registration
# @method_decorator(csrf_exempt, name='dispatch')
# class Authentication(View):
#     def post(self, request):
#         # getting api data
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#
#         form = UserForm(body)
#
#         if form.is_valid():
#             instance = form.save()
#             # user = authenticate(username=instance._meta.fields['username'], password=instance._meta.fields['password'])
#             # login(user)
#             # print('login okk.')
#             return JsonResponse(model_to_dict(instance, fields=[field.name for field in instance._meta.fields]))
#         else:
#             return JsonResponse({"errors": form.errors.as_json()}, status=422)
