from django import forms
from .models import Quiz, Question, Answer
from django.contrib import admin
from django.forms import ModelForm,TextInput,NumberInput,HiddenInput,ComboField,Select

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'desc', 'number_of_questions', 'time')

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Назва тесту"

            }),
            "desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Опис"

            }),
            "number_of_questions": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Кількість питань"
            }),
            "time": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Час відведений для тесту"

        })

        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'quiz')

        widgets = {
            "content": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Назва тесту"

            }),
            "quiz": Select(attrs={
                'class': 'form-control',
            })
        }


# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ('content', 'correct', 'question')
#
#         widgets = {
#             "content": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': "Назва тесту"
#
#             })}
