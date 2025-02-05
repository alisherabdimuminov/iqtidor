from django.http import HttpRequest
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import (
    User,
    Subject,
)
from .serializers import (
    SubjectSerializer,
)


@decorators.api_view(http_method_names=["POST"])
def login(request: HttpRequest):
    username = request.data.get("phone")
    password = request.data.get("password")

    user = User.objects.filter(username=username)

    if not user.exists():
        return Response({
            "status": "error",
            "code": "404",
            "data": "Foydalanuvchi topilmadi",
        })
    
    user = user.first()

    if not user.check_password(password):
        return Response({
            "status": "error",
            "code": "400",
            "data": "Noto'g'ri parol",
        })
    
    tokens = Token.objects.filter(user=user)
    tokens.delete()

    token = Token.objects.create(user=user)

    return Response({
        "status": "success",
        "code": "200",
        "data": {
            "phone": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "middle_name": user.middle_name,
            "city": user.city,
            "town": user.town,
            "rural": user.rural,
            "school": user.school,
            "token": token.key,
        }
    })


@decorators.api_view(http_method_names=["POST"])
def signup(request: HttpRequest):
    username = request.data.get("phone")
    password = request.data.get("password")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    middle_name = request.data.get("middle_name")
    city = request.data.get("city")
    town = request.data.get("town")
    rural = request.data.get("rural")
    school = request.data.get("school")

    user = User.objects.filter(username=username)

    if user.exists():
        return Response({
            "status": "error",
            "code": "400",
            "data": "Bu telefon raqami allaqachon ro'yxatdan o'tgan."
        })
    
    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        city=city,
        town=town,
        rural=rural,
        school=school,
    )

    user.set_password(password)
    user.save()

    return Response({
        "status": "success",
        "code": "200",
        "data": ""
    })


@decorators.api_view(http_method_names=["GET"])
def get_subjects(request: HttpRequest):
    subjects_obj = Subject.objects.all()
    subjects = SubjectSerializer(subjects_obj, many=True)
    return Response({
        "status": "success",
        "code": "200",
        "data": {
            "subjects": subjects.data,
        }
    })
