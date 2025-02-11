from django.contrib import admin
from unfold import admin as unfold_admin
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import (
    DTM,
    Block,
    Subject,
    DTMQuestion,
)


class DTMQuestionInline(unfold_admin.StackedInline):
    model = DTMQuestion
    extra = 0


@admin.register(DTM)
class DTMModelAdmin(unfold_admin.ModelAdmin):
    list_display = ["name", "count_participants", ]
    search_fields = ["name", ]


@admin.register(Block)
class BlockModelAdmin(unfold_admin.ModelAdmin):
    list_display = ["name", "subject", "count_questions", ]
    inlines = [DTMQuestionInline, ]
    search_fields = ["name", ]
    list_filter = ["subject", ]


@admin.register(Subject)
class SubjectModelAdmin(unfold_admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(DTMQuestion)
class DTMQuestionModelAdmin(unfold_admin.ModelAdmin):
    list_display = ["block", "question_", "correct_answer", ]
    list_filter = ["block", ]
    search_fields = ["question", ]

    def question_(self, obj):
        return mark_safe(obj.question)
