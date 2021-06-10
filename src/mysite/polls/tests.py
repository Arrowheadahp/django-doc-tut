from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from .models import question

class questionModelTests(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)