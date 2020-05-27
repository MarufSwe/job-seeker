from django.urls import path, include
from . import views

urlpatterns = [
    path('personal-info/', views.personal_information),
    path('professional-info/', views.professional_information),
    path('add-per-info/', views.create_personal_info),
    path('del-per-info/<int:id>/', views.delete_personal_info),

    path('add-pro-info/', views.create_professional_info),
    path('del-pro-info/<int:id>/', views.delete_professional_info),

]

