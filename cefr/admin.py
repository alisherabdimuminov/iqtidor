from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline


from .models import Subject, Answer, CEFR, Question


class AnswerInline(StackedInline):
    model = Answer
    extra = 4


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ["name"]


@admin.register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = ["value_1", "value_2", "is_correct"]


@admin.register(CEFR)
class CEFRAdmin(ModelAdmin):
    list_display = ["name", "description", "subject"]


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ["cefr", "question"]
    inlines = [AnswerInline]
