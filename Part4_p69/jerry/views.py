# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'jerry/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('jerry:results', args=(question.id,)))
