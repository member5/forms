from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
	list_display = ['id','title','description']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ['id','text', 'form']
