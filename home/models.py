from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.


class Diseases(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='TODO')

    def __str__(self):
        return self.name


class Questions(models.Model):
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class QuestionChoices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text
