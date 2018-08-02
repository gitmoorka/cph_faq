from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Answer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def question_list(request):
    question = Question.objects.all()
    return render(request, 'faq/question_list.html', {'question': question})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'faq/question_detail.html', {'question': question})







