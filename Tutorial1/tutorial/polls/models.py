# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Question(models.Model):
	#def was_published_recently(self):
	#	return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
	#______________________
	def __str__(self):
		return self.question_text
	#_______________________________________	
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now
	
class Choice(models.Model):
	
	def __str__(self):
		return self.choice_text
	#___________________________________
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

