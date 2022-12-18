from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Diseases, Questions, QuestionChoices
from .forms import Lung_Cancer_Quiz
from .lung_cancer_predict import predict_lung_cancer

def home_site(request):
    html = 'home/homepage.html'
    diseases = Diseases.objects.all()
    return render(request, html, {'diseases': diseases})


def disease(request, disease_id):
    # if lung cancer
    if disease_id == 1:
        html = 'home/lung_cancer_quiz.html'
    else:
        html = 'home/heart_disease_quiz.hml'
    disease = get_object_or_404(Diseases, id=disease_id)
    questions = Questions.objects.filter(disease_id=disease_id)
    choices = QuestionChoices.objects
    return render(request, html, {'disease': disease, 'questions': questions, 'choices': choices})


def results(request, disease_id):
    print(request.POST)
    if disease_id == 1:
        age = request.POST['age']
        gender = request.POST['gender']
        level = request.POST['level']
        prediction = predict_lung_cancer(age, gender, level)[0]

    html = 'home/results.html'
    disease = get_object_or_404(Diseases, id=disease_id)
    return render(request, html, {'disease': disease, 'prediction':prediction})



