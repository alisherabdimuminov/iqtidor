from rest_framework import serializers

from .models import (
    Answer,
    CEFR,
    Question,
    Subject,
)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

    
class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField("get_answers")

    def get_answers(self, obj):
        answers = Answer.objects.filter(question=obj)
        serializer = AnswerSerializer(answers, many=True)
        return serializer.data

    class Meta:
        model = Question
        fields = ("id", "cefr", "question", "answers")


class CefrSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    def get_fields(self):
        fields = super().get_fields()
        if self.context.get("list"):
            fields.pop("questions", None)
        return fields

    def get_questions(self, obj):
        questions = Question.objects.filter(cefr=obj)
        serializer = QuestionSerializer(questions, many=True)
        return serializer.data

    class Meta:
        model = CEFR
        fields = ("id", "name", "description", "subject", "questions")

