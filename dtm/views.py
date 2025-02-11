from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import (
    Block,
    DTM,
    DTMQuestion,
    Subject,
)
from .serializers import (
    BlockSerializer,
    DTMQuestionSerializer,
    DTMSerializer,
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
@decorators.authentication_classes([TokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
def get_dtms(request):
    dtms = DTM.objects.all()
    serializer = DTMSerializer(dtms, many=True, context={"list": True, "request": request})
    return Response({
        "status": "success",
        "code": "200",
        "data": serializer.data,
    })


@decorators.api_view(http_method_names=["GET"])
@decorators.authentication_classes([TokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
def get_dtm(request, dtm_id):
    dtm = DTM.objects.get(id=dtm_id)
    serializer = DTMSerializer(dtm, context={"request": request})
    return Response({
        "status": "success",
        "code": "200",
        "data": serializer.data,
    })


@decorators.api_view(http_method_names=["POST"])
@decorators.authentication_classes([TokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
def paticipate_dtm(request, dtm_id):
    dtm = DTM.objects.get(id=dtm_id)
    user = request.user
    dtm.participants.add(user)
    dtm.participants.save()
    dtm.save()
    return Response({
        "status": "success",
        "code": "200",
        "data": "Successfully participated",
    })
    

