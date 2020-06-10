from django.urls import path
from .views import (

    ViewProfessionals,
    ViewPersonals,
    ViewAcademics,
    ViewDegree,
    ViewEducationLevel,
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
# education level api
    path('api/education-level/', ViewEducationLevel.as_view()),
# degree api
    path('api/degree/', ViewDegree.as_view()),
    path('api/degree/<int:id>', ViewDegree.as_view()),
# professionals api
    path('api/professionals/', ViewProfessionals.as_view()),
    path('api/professionals/<int:id>', ViewProfessionals.as_view()),
# personals api
    path('api/personals/', ViewPersonals.as_view()),
    path('api/personals/<int:id>', ViewPersonals.as_view()),
# academics api
    path('api/academics/', ViewAcademics.as_view()),
    path('api/academics/<int:id>', ViewAcademics.as_view()),

)
