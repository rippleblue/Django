# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
	return HttpResponse("Hello!")

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'jerry/detail.html',{'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s. " 
	return HttpResponse(response % question_id)

def vote(request, question_id):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list' : latest_question_list}
	return render(request, 'jerry/index.html', context)
