from django.db import models

import datetime
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class question(models.Model):
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.q_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # def get_absolute_url(self):
    #     return reverse('polls:detail', kwargs={'pk': self.id})

    # def get_vote_url(self):
    #     return reverse('polls:vote', kwargs={'pk': self.id})

    # def get_results_url(self):
    #     return reverse('polls:results', kwargs={'pk': self.id})




class choice(models.Model):
    quest = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
