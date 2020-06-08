from django.urls import path
from .views import (

ViewProfessionals,
    ViewPersonals,
    ViewAcademics
    # Authentication
)

from .views import login, logout, sign_up

urlpatterns = (
    # sign-up api
    path('sign-up/', sign_up),
    #
    # # login api
    path('login/', login),
    #
    # # logout api
    path('logout/', logout),

    path('api/professionals/', ViewProfessionals.as_view()),
    path('api/professionals/<int:id>', ViewProfessionals.as_view()),

    path('api/personals/', ViewPersonals.as_view()),

    path('api/personals/<int:id>', ViewPersonals.as_view()),

    path('api/academics/', ViewAcademics.as_view()),

    path('api/academics/<int:id>', ViewAcademics.as_view()),

)
