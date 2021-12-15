from django.urls import path
from . import views
from django.urls import path

from .views import HomePageView, SearchResultsView, SearchResultsscoreView, SearchResultsQuizView, edit

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:myid>/", views.quiz, name="quiz"),
    path('<int:myid>/data/', views.quiz_data_view, name='quiz-data'),
    path('<int:myid>/save/', views.save_quiz_view, name='quiz-save'),
    
    # path("signup/", views.Signup, name="signup"),
    # path("login/", views.Login, name="login"),
    # path("logout/", views.Logout, name="logout"),
    
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('add_question/', views.add_question, name='add_question'),
    path('add_options/<int:myid>/', views.add_options, name='add_options'),
    path('results/', views.results, name='results'),
    path('delete_question/<int:myid>', views.delete_question, name='delete_question'),
    path('delete_result/<int:myid>/', views.delete_result, name='delete_result'),
    path('delete_quiz/<int:myid>', views.delete_quiz, name='delete_quiz'),
    # path('<pk>/delete/',views.CourseDeleteView.as_view(),  name='course_delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search2/', SearchResultsscoreView.as_view(), name='search_resultsscore'),
    path('searchQuiz/', SearchResultsQuizView.as_view(), name='search_resultsQuiz'),
    path('edit/<int:id>/', views.edit, name='edit'),
    # path('home/', HomePageView.as_view(), name='home'),
]