from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import QuizForm, QuestionForm
from django.forms import inlineformset_factory
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.db.models import Q

from .models import Question


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsQuizView(ListView):
    model = Quiz
    template_name = 'search_resultsQuiz.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Quiz.objects.filter(
            Q(name__icontains=query)
        ).values()
        return object_list

class SearchResultsView(ListView):
    model = Question
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Question.objects.filter(
            Q(quiz__name__icontains=query)
        )
        return object_list

class SearchResultsscoreView(ListView):
    model = Marks_Of_User
    template_name = 'search_resultsscore.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Marks_Of_User.objects.filter(
            Q(user__username__icontains=query)
        )
        return object_list

def index(request):
    quiz = Quiz.objects.all()
    para = {'quiz' : quiz}
    return render(request, "index.html", para)

@login_required(login_url = '/login')
def quiz(request, myid):
    quiz = Quiz.objects.get(id=myid)
    return render(request, "quiz.html", {'quiz':quiz})

def quiz_data_view(request, myid):
    quiz = Quiz.objects.get(id=myid)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.content)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, myid):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(content=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(id=myid)

        score = 0
        marks = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.content)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.content:
                        if a.correct:
                            score += 1
                            correct_answer = a.content
                    else:
                        if a.correct:
                            correct_answer = a.content

                marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                marks.append({str(q): 'not answered'})
     
        Marks_Of_User.objects.create(quiz=quiz, user=user, score=score)
        
        return JsonResponse({'passed': True, 'score': score, 'marks': marks})
    

# def Signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method=="POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         password = request.POST['password1']
#         confirm_password = request.POST['password2']
#
#         if password != confirm_password:
#             return redirect('/register')
#
#         user = User.objects.create_user(username, email, password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
#         return render(request, 'login.html')
#     return render(request, "signup.html")
#
# def Login(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             return render(request, "login.html")
#     return render(request, "login.html")
#
# def Logout(request):
#     logout(request)
#     return redirect('/')


def add_quiz(request):
    quiz = Quiz.objects.all()
    para = Quiz.objects.filter().order_by('-id')
    # return render(request, "add_quiz.html", para)
    if request.method=="POST":
        form = QuizForm(data=request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            obj = form.instance

            return render(request, "add_quiz.html", {'obj':obj})
    else:

        form=QuizForm()
    return render(request, "add_quiz.html",  {'form':form, 'quiz':para})


def add_question(request):
    questions = Question.objects.all()
    questions = Question.objects.filter().order_by('-id')
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "add_question.html")
    else:
        form=QuestionForm()
    return render(request, "add_question.html", {'form':form, 'questions':questions})

def delete_quiz(request, myid):
    para = Quiz.objects.get(id=myid)
    if request.method == "POST":
        para.delete()
        return redirect('add_quiz')
    return render(request, "delete_quiz.html", {'quiz':para})

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('add_question')
    return render(request, "delete_question.html", {'question':question})


def add_options(request, myid):
    question = Question.objects.get(id=myid)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content','correct', 'question'), extra=4)
    if request.method=="POST":
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "add_options.html", {'alert':alert})
    else:
        formset=QuestionFormSet(instance=question)
    return render(request, "add_options.html", {'formset':formset, 'question':question})

def results(request):
    marks = Marks_Of_User.objects.order_by('-date')
    return render(request, "results.html", {'marks':marks})

def delete_result(request, myid):
    mark = Marks_Of_User.objects.get(id=myid)
    if request.method == "POST":
        mark.delete()
        return redirect('results')
    return render(request, "delete_result.html", {'mark':mark})


def edit(request, id):

    try:
        person = Quiz.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.desc = request.POST.get("desc")
            person.number_of_questions = request.POST.get("number_of_questions", default=None)
            person.time = request.POST.get("time")
            person.save()
            return redirect('add_quiz')
        else:
            return render(request, "edit.html", {"person": person})
    except Quiz.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")