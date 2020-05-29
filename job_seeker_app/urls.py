from django.urls import path
from . import views
from .views import (

    ViewProfessionalsList,
    ViewProfessionalsAdd,
    ViewProfessionalsUpdate,
    ViewProfessionalsDelete,
    ViewUserRegistration,
    ViewPersonalsList,
    ViewPersonalsAdd,
    ViewPersonalsUpdate,
    ViewPersonalsDelete,
    ViewAcademicsList,
    ViewAcademicsAdd,
    ViewAcademicsUpdate,
    ViewAcademicsDelete,
)

urlpatterns = [

    path('registration/', ViewUserRegistration.as_view()),
    path('api/professionals-list/', ViewProfessionalsList.as_view()),
    path('api/professionals-add/', ViewProfessionalsAdd.as_view()),
    path('api/professionals-update/<int:id>', ViewProfessionalsUpdate.as_view()),
    path('api/professionals-delete/<int:id>', ViewProfessionalsDelete.as_view()),

    path('api/personals-list/', ViewPersonalsList.as_view()),
    path('api/personals-add/', ViewPersonalsAdd.as_view()),
    path('api/personals-update/<int:id>', ViewPersonalsUpdate.as_view()),
    path('api/personals-delete/<int:id>', ViewPersonalsDelete.as_view()),
    path('api/academics-list/', ViewAcademicsList.as_view()),
    path('api/academics-add/', ViewAcademicsAdd.as_view()),
    path('api/academics-update/<int:id>', ViewAcademicsUpdate.as_view()),
    path('api/academics-delete/<int:id>', ViewAcademicsDelete.as_view()),

]
