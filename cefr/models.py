from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import User


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Fan nomi")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"
    

class CEFR(models.Model):
    name = models.CharField(max_length=255, verbose_name="CEFR nomi")
    description = RichTextUploadingField(verbose_name="Tavsif")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="cefr_subject", verbose_name="Fan")
    participants = models.ManyToManyField(User, related_name="cefr_participants", verbose_name="Qatnashchilar", blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Narx")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "CEFR"
        verbose_name_plural = "CEFR"


class Question(models.Model):
    cefr = models.ForeignKey(CEFR, on_delete=models.CASCADE, related_name="cefr_questions", verbose_name="CEFR")
    question = RichTextUploadingField(verbose_name="Savol")
    # point = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ball")

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer_question", verbose_name="Savol")
    value_1 = models.CharField(max_length=255, verbose_name="1-qiymat")
    value_2 = models.CharField(max_length=255, verbose_name="2-qiymat", null=True, blank=True)
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri javob")

    def __str__(self):
        return self.value_1
    
    class Meta:
        verbose_name = "Javob"
        verbose_name_plural = "Javoblar"
