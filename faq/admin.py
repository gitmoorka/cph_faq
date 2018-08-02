from django.contrib import admin

# Register your models here.

from .models import Question, Answer, AnswerVote, QuestionVote

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerVote)
admin.site.register(QuestionVote)