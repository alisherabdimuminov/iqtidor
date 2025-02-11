from rest_framework import serializers


from .models import (
    Block,
    DTM,
    DTMQuestion,
    Subject,
)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class DTMQuestionSerializer(serializers.ModelSerializer):
    point = serializers.FloatField()
    class Meta:
        model = DTMQuestion
        fields = "__all__"


class BlockSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    questions = serializers.SerializerMethodField("get_questions")

    def get_fields(self):
        fields = super().get_fields()
        if self.context.get("list"):
            fields.pop("questions", None)
        return fields

    def get_questions(self, obj):
        questions = DTMQuestion.objects.filter(block=obj)
        return DTMQuestionSerializer(questions, many=True).data

    class Meta:
        model = Block
        fields = ["id", "subject", "questions"]

    
class DTMQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DTMQuestion
        fields = "__all__"


class DTMSerializer(serializers.ModelSerializer):
    block_1 = BlockSerializer()
    block_2 = BlockSerializer()
    block_3 = BlockSerializer()
    block_4 = BlockSerializer()
    block_5 = BlockSerializer()
    is_participant = serializers.SerializerMethodField("get_is_participant")

    def get_is_participant(self, obj):
        request = self.context.get("request")
        if request:
            return obj.participants.filter(id=request.user.id).exists()
        return False

    class Meta:
        model = DTM
        fields = ("id", "name", "duration", "price", "is_participant", "block_1", "block_2", "block_3", "block_4", "block_5", "count_participants")
