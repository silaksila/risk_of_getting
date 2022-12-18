from django import forms
from .models import Diseases, Questions, QuestionChoices


class Lung_Cancer_Quiz(forms.Form):
    age = forms.CharField(label="Your age: ", max_length=5)
    gender = forms.ChoiceField(label='Gender: ', choices=('Male', 'Female', 'Other'))
    air_pollution = forms.ChoiceField(label="Air pollution level: ", choices=range(1, 11))

