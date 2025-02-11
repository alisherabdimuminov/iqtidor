from rest_framework import decorators
from rest_framework.response import Response

from .models import (
    Answer,
    CEFR,
    Question,
    Subject,
)
from .serializers import (
    AnswerSerializer,
    CefrSerializer,
    QuestionSerializer,
    SubjectSerializer,
)


@decorators.api_view(http_method_names=["GET"])
def get_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response({
        "status": "success",
        "code": "200",
        "data": serializer.data,
    })


@decorators.api_view(http_method_names=["GET"])
def get_cefrs(request, subject_id):
    cefrs = CEFR.objects.filter(subject_id=subject_id)
    serializer = CefrSerializer(cefrs, many=True, context={"list": True, "request": request})
    return Response({
        "status": "success",
        "code": "200",
        "data": serializer.data,
    })


@decorators.api_view(http_method_names=["GET"])
def get_cefr(request, subject_id, cefr_id):
    cefr = CEFR.objects.get(id=cefr_id)
    serializer = CefrSerializer(cefr, context={"request": request})
    return Response({
        "status": "success",
        "code": "200",
        "data": serializer.data,
    })
