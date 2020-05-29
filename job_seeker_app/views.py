from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
import jwt, json
from rest_framework import views
from rest_framework.response import Response

from .models import (
    Personals,
    Professionals,
    Academics,
    Degree,

)

#
# class Login(views.APIView):
#
#     def post(self, request):
#         if not request.data:
#             return Response({'Error': "Please provide username/password"}, status="400")
#
#         username = request.data['username']
#         password = request.data['password']
#         try:
#             user = User.objects.get(username=username, password=password)
#             print(user)
#         except User.DoesNotExist:
#             return Response({'Error': "Invalid username/password"}, status="400")
#         if user:
#             payload = {
#                 'id': user.id,
#                 'email': user.email,
#             }
#             jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
#
#             return HttpResponse(
#                 json.dumps(jwt_token),
#                 status=200,
#                 content_type="application/json"
#         )
#         else:
#             return Response(
#             json.dumps({'Error': "Invalid credentials"}),
#             status=400,
#             content_type="application/json"
#         )


@method_decorator(csrf_exempt, name='dispatch')
class ViewUserRegistration(View):
    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        id = body['id']
        username = body['username']
        password = body['password']
        email = body['email']
        first_name = body['first_name']
        last_name = body['last_name']

        if id and username and password and email and first_name and last_name:
            User.objects.create(
                id=id,
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            return JsonResponse({'message': 'Registration Successfully Complete !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": " Data Not Found!"}, status=404, safe=False)


# Professionals API CRUD

@method_decorator(csrf_exempt, name='dispatch')
class ViewProfessionalsList(View):
    def get(self, request):
        data = {
            "professionals_list": list(Professionals.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewProfessionalsAdd(View):
    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        organization_name = body['organization_name']
        organization_type = body['organization_type']
        department = body['department']
        designation = body['designation']
        responsibilities = body['responsibilities']
        employment_from = body['employment_from']
        employment_to = body['employment_to']
        company_location = body['company_location']
        user_id = body['user_id']

        exiting_user = User.objects.get(id=user_id)

        if organization_name and organization_type and department and designation and responsibilities and employment_from and employment_to and company_location and user_id:
            Professionals.objects.create(
                organization_name=organization_name,
                organization_type=organization_type,
                department=department,
                designation=designation,
                responsibilities=responsibilities,
                employment_from=employment_from,
                employment_to=employment_to,
                company_location=company_location,
                user_id=exiting_user,
            )
            return JsonResponse({'message': 'Professional Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewProfessionalsUpdate(View):
    def put(self, request, id=None):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            organization_name = body['organization_name']
            organization_type = body['organization_type']
            professionals = get_object_or_404(Professionals, id=id)
            professionals.organization_name = organization_name
            professionals.organization_type = organization_type
            professionals.save()

            return JsonResponse({"message": "Updated!"}, status=201, safe=False)

        except Professionals.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
# class ViewProfessionalsUpdate(View):
#     def put(self, request, id=None):
#         try:
#             body_unicode = request.body.decode('utf-8')
#             body = json.loads(body_unicode)
#             organization_name = body['organization_name']
#             organization_type = body['organization_type']
#             # department = body['department']
#             # designation = body['designation']
#             # responsibilities = body['responsibilities']
#             # employment_from = body['employment_from']
#             # employment_to = body['employment_to']
#             # company_location = body['company_location']
#             professionals = get_object_or_404(Professionals, id=id)
#             professionals.organization_name = organization_name
#             professionals.organization_type = organization_type
#             # professionals.department = department
#             # professionals.designation = designation
#             # professionals.responsibilities = responsibilities
#             # professionals.employment_from = employment_from
#             # professionals.employment_to = employment_to
#             # professionals.company_location = company_location
#             professionals.save()
#
#             return JsonResponse({"message": "Updated!"}, status=201, safe=False)
#
#         except Personals.DoesNotExist as e:
#             return JsonResponse({"message": e}, status=404, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class ViewProfessionalsDelete(View):
    def delete(self, request, id):
        professionals = get_object_or_404(Professionals, id=id)
        if professionals:
            professionals.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


# Personals API CRUD
@method_decorator(csrf_exempt, name='dispatch')
class ViewPersonalsList(View):
    def get(self, request):
        data = {
            "personals_list": list(Personals.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewPersonalsAdd(View):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_id = body['user_id']
        first_name = body['first_name']
        last_name = body['last_name']
        fathers_name = body['fathers_name']
        mothers_name = body['mothers_name']
        date_of_birth = body['date_of_birth']
        email = body['email']
        gender = body['gender']
        religion = body['religion']
        nid = body['nid']

        exiting_user = User.objects.get(id=user_id)

        if first_name and last_name and fathers_name and mothers_name and date_of_birth and email and gender and religion and nid and user_id:
            Personals.objects.create(
                first_name=first_name,
                last_name=last_name,
                fathers_name=fathers_name,
                mothers_name=mothers_name,
                date_of_birth=date_of_birth,
                email=email,
                gender=gender,
                religion=religion,
                nid=nid,
                user_id=exiting_user,
            )
            return JsonResponse({'message': 'Personal Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewPersonalsUpdate(View):
    def put(self, request, id=None):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            first_name = body['first_name']
            last_name = body['last_name']
            personals = get_object_or_404(Personals, id=id)
            personals.first_name = first_name
            personals.last_name = last_name
            personals.save()

            return JsonResponse({"message": "Updated!"}, status=201, safe=False)

        except Personals.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewPersonalsDelete(View):
    def delete(self, request, id=None):
        personals = get_object_or_404(Personals, id=id)
        if personals:
            personals.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


# Academics CRUD

@method_decorator(csrf_exempt, name='dispatch')
class ViewAcademicsList(View):
    def get(self, request):
        data = {
            "academics_list": list(Academics.objects.values())
        }

        if data:
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewAcademicsAdd(View):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_id = body['user_id']
        degree = body['degree']

        board = body['board']
        institution = body['institution']
        result = body['result']
        year = body['year']

        exiting_user = User.objects.get(id=user_id)
        exiting_degree = Degree.objects.get(id=degree)

        if user_id and degree and board and institution and result and year:
            Academics.objects.create(
                user_id=exiting_user,
                degree=exiting_degree,
                board=board,
                institution=institution,
                result=result,
                year=year,
            )
            return JsonResponse({'message': 'Academics Info Added !'}, status=201, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewAcademicsUpdate(View):
    def put(self, request, id=None):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            board = body['board']
            institution = body['institution']
            academics = get_object_or_404(Academics, id=id)
            academics.board = board
            academics.institution = institution
            academics.save()

            return JsonResponse({"message": "Updated!"}, status=201, safe=False)

        except Academics.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ViewAcademicsDelete(View):
    def delete(self, request, id=None):
        academics = get_object_or_404(Academics, id=id)
        if academics:
            academics.delete()
            return JsonResponse({"message": "Deleted!"}, status=200, safe=False)
        else:
            return JsonResponse({"message": "Not Found!"}, status=404, safe=False)
