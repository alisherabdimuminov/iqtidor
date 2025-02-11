from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import User


ANSWER_CHOICES = (
    ("a", "A Variant"),
    ("b", "B Variant"),
    ("c", "C Variant"),
    ("d", "D Variant"),
)



class Subject(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Fan nomi")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fanlar"
        verbose_name_plural = "Fanlar"
    

class Block(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Fan blok nomi")
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="dtm_questions", verbose_name="Fan")

    def questions(self):
        return DTMQuestion.objects.filter(block=self)
    
    def count_questions(self):
        return DTMQuestion.objects.filter(block=self).count()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fan bloklar"
        verbose_name_plural = "Fan bloklar"


class DTMQuestion(models.Model):
    block = models.ForeignKey("Block", on_delete=models.CASCADE, related_name="questions", verbose_name="Fan blok")
    question = RichTextUploadingField(verbose_name="Savol")
    answer_a = RichTextUploadingField(verbose_name="A Variant")
    answer_b = RichTextUploadingField(verbose_name="B Variant")
    answer_c = RichTextUploadingField(verbose_name="C Variant")
    answer_d = RichTextUploadingField(verbose_name="D Variant")
    correct_answer = models.CharField(max_length=1000, verbose_name="To'g'ri javob", choices=ANSWER_CHOICES)
    point = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ball")

    def __str__(self):
        return "self.question"
    
    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class DTM(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Test nomi")
    duration = models.IntegerField(verbose_name="Vaqt (minut)", default=90)
    block_1 = models.ForeignKey("Block", on_delete=models.CASCADE, related_name="dtm_block_1", verbose_name="Fan blok 1")
    block_2 = models.ForeignKey("Block", on_delete=models.CASCADE, related_name="dtm_block_2", verbose_name="Fan blok 2")
    block_3 = models.ForeignKey("Block", on_delete=models.CASCADE, related_name="dtm_block_3", verbose_name="Fan blok 3")
    block_4 = models.ForeignKey("Block", on_delete=models.CASCADE, related_name="dtm_block_4", verbose_name="Fan blok 4")
    block_5 = models.ForeignKey("Block", on_delete=models.CASCADE, related_name="dtm_block_5", verbose_name="Fan blok 5")
    participants = models.ManyToManyField(User, related_name="dtm_participants", blank=True, verbose_name="Qatnashchilar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi", default=0)

    def count_participants(self):
        return self.participants.count()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"


class DTMResult(models.Model):
    dtm = models.ForeignKey(DTM, on_delete=models.CASCADE, related_name="results", verbose_name="Test")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dtm_results", verbose_name="Foydalanuvchi")
    point = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ball")
    cases = models.JSONField(default=dict, verbose_name="Javoblar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return f"{self.user} - {self.dtm}"
