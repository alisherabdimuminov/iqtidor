from django.contrib import admin

from .models import (
    Answer,
    Question,
    Subject,
    User,
)



@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ["value_1", "value_2", "is_correct", ]


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["subject", "question", "point", ]
