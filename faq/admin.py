from django.contrib import admin

# Register your models here.

from .models import Question, Answer, AnswerVote, QuestionVote


admin.register(Question)
admin.register(Answer)
admin.register(AnswerVote)
admin.register(QuestionVote)