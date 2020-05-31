from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('personal_info/', views.personal_information),
    path('add_per_info/', views.create_personal_info),
    path('update_per_info/<int:id>/', UpdatePersonalInfo.as_view()),
    path('del_per_info/<int:id>/', views.delete_personal_info),

    path('professional_info/', views.professional_information),
    path('add_pro_info/', views.create_professional_info),
    path('update_pro_info/<int:id>/', UpdateProfessionalInfo.as_view()),
    path('del_pro_info/<int:id>/', views.delete_professional_info),

    path('degree/', views.degree_name),
    path('add_degree/', views.create_degree),
    path('update_degree/<int:id>/', UpdateDegree.as_view()),
    path('del_degree/<int:id>/', views.delete_degree),

    path('academic_info/', views.academic_info_list),
    path('add_academic_info/', views.create_academic_info),
    path('update_academic/<int:id>/', UpdateAcademicInfo.as_view()),
    path('del_academic/<int:id>/', views.delete_academic_info),

    path('seeker_list/', views.job_seeker_list),
    path('registration/', JobSeekerRegistration.as_view()),

]

