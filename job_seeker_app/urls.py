from django.urls import path, include
from . import views
from .views import UpdateProfessionalInfo, UpdatePersonalInfo, UpdateDegree

urlpatterns = [
    path('personal_info/', views.personal_information),
    path('add-per_info/', views.create_personal_info),
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

]

