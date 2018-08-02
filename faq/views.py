from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Question, Answer



def index(request):
    return render_to_response('faq/home.html')



class QuestionDetailView(DetailView):

    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class QuestionListView(ListView):

    model = Question
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





