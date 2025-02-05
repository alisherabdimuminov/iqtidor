from rest_framework import serializers

from .models import (
    User,
    Subject,
    Answer,
    CEFR,
    DTM,
    Question,
    CEFRResult,
    Block,
    DTMResult,
)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", )


class DTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = DTM
        fields = ("name", "block_1", "block_2", "block_3", "block_4", "block_5", )


class CEFRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEFR
        fields = ("cefr", )
