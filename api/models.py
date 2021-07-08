from django.db import models


# Create your models here.
class Form(models.Model):
	title = models.CharField(max_length=60)
	description = models.CharField(max_length=200, null=True, blank=True)
	text = models.CharField(max_length=200, null=True, blank=True) 

	def __str__(self):
		return self.title


class Question(models.Model):
	text = models.CharField(max_length=200)
	form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form_question")

	def __str__(self):
		return self.text
