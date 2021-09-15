from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from polls.models import Choice, Question


class IndeXView(LoginRequiredMixin, ListView):
    """Render 5 most recent polls """

    login_url = 'login'
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, DetailView):
    """ Render details of a single poll"""
    
    login_url = 'login'
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    """ Render result of a single poll"""
    
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    """ Performs voting for a poll """

    user = request.user
    print(user)
    if not user.is_authenticated:
        return redirect('login')

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question' : question,
            'error_message' : "You didn't select a choice."
        }
        return render(request, 'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(question.id,)))
