from django.db import models
from django.utils.text import slugify


class Question(models.Model):
    question_text = models.TextField(default="")
    slug = models.SlugField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(default="")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text

class VoteParent(models.Model):
    """Abstract model to define the basic elements to every single vote."""
    value = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AnswerVote(VoteParent):
    """Model class to contain the votes for the answers."""
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class QuestionVote(VoteParent):
    """Model class to contain the votes for the questions."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


