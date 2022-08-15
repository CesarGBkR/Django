from pyexpat import model
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
