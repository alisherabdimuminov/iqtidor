from django.urls import path

from .views import (
    get_subjects,

    login,
    signup,
)


urlpatterns = [
    path("auth/login/", login,),
    path("auth/signup/", signup,),

    path("subjects/", get_subjects,),
]
