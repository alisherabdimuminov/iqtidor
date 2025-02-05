from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=1000, unique=True)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    middle_name = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    town = models.CharField(max_length=1000)
    rural = models.CharField(max_length=1000)
    school = models.CharField(max_length=1000)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
    

class Subject(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    

class Answer(models.Model):
    value_1 = models.TextField()
    value_2 = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.value_1


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField()
    answers = models.ManyToManyField(Answer, related_name="question_answers")
    point = models.DecimalField(max_digits=10, decimal_places=2, default=2)

    def __str__(self):
        return self.question


class Block(models.Model):
    name = models.CharField(max_length=1000)
    questions = models.ManyToManyField(Question, related_name="block_questions")

    def __str__(self):
        return self.name


class DTM(models.Model):
    name = models.CharField(max_length=1000)
    block_1 = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="dtm_block_1")
    block_2 = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="dtm_block_2")
    block_3 = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="dtm_block_3")
    block_4 = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="dtm_block_4")
    block_5 = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="dtm_block_5")
    participants = models.ManyToManyField(User, related_name="dtm_participants", blank=True)

    def __str__(self):
        return self.name
    
    def count_participants(self):
        return self.participants.count()


class CEFR(models.Model):
    name = models.CharField(max_length=1000)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name="cefr_questions")
    participants = models.ManyToManyField(User, related_name="cefr_participants", blank=True)
    duration = models.IntegerField(default=60)

    def __str__(self):
        return self.name
    
    def count_questions(self):
        return self.questions.count()
    
    def count_participants(self):
        return self.participants.count()


class DTMResult(models.Model):
    dtm = models.ForeignKey(DTM, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cases = models.JSONField(default=list)
    correct = models.IntegerField(default=0)
    score = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.score)
    

class CEFRResult(models.Model):
    cefr = models.ForeignKey(CEFR, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cases = models.JSONField(default=list)
    correct = models.IntegerField(default=0)
    score = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.score)
