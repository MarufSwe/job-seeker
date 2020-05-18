from django.urls import path, include
from . import views

urlpatterns = [
    path('personal-info/', views.personal_information),
    path('professional-info/', views.professional_information),


]
