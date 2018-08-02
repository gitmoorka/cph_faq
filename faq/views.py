from django.shortcuts import get_object_or_404, render
from .models import Question, Answer
from django.shortcuts import render_to_response



def index(request):
    return render_to_response('faq/home.html')

def question_list(request):
    question = Question.objects.all()
    return render(request, 'faq/question_list.html', {'question': question})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'faq/question_detail.html', {'question': question})







