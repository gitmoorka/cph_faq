from django.urls import path

from . import views

from faq.views import QuestionDetailView, QuestionListView


app_name = 'faq'

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', QuestionListView.as_view(), name='list'),
    path('<slug:slug>/', QuestionDetailView.as_view(), name='question-detail'),
    # path('question/<int:pk>/', views.question_detail, name='detail'),
    # path('all/', views.question_list, name='list'),
]