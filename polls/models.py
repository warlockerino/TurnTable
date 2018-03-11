import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime
from django.urls import reverse

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answers = 0

    def get_date(self):
        time = datetime.now()
        if self.pub_date.day == time.day:
            return str(time.hour - self.pub_date.hour) + " hours ago"
        else:
            if self.pub_date.month == time.month:
                return str(time.day - self.pub_date.day) + " days ago"
            else:
                if self.pub_date.year == time.year:
                    return str(time.month - self.pub_date.month) + " months ago"
        return self.pub_date

    def get_votes(self):

        answers = 0
        for c in Choice.objects.filter(question = self.id):
            answers += c.votes
        return answers

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={ 'pk': str(self.id) })


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
