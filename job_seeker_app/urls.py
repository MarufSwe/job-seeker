from django.urls import path, include
from . import views

urlpatterns = [
    path('personal-info/', views.personal_information),
    path('professional-info/', views.professional_information),
    path('add-personal-info/', views.create_personal_info),
    path('del-per-info/<int:id>/', views.delete_professional_info),


]

