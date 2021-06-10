from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls.base import reverse
from .models import question, choice
from django.shortcuts import get_object_or_404

from django.views.generic import (
    DetailView, 
    ListView,
)

# def index(request):
#     latest_question_list = question.objects.order_by('-pub_date')[:5][::-1]
#     # return HttpResponse(', '.join([q.q_text for q in latest_question_list]))
#     return render(request, 'polls/index.html', context={'latest_question_list': latest_question_list})


# def detail(request, pk):
#     # return HttpResponse(f'You\'re looking at poll number {pk}')
#     q = get_object_or_404(question, id=pk)
#     return render(request, 'polls/detail.html', context={'poll': q})



# def results(request, pk):
#     q = get_object_or_404(question, id=pk)
#     return render(request, 'polls/results.html', context={'poll': q})









class indexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    queryset = question.objects.all().order_by('-pub_date')[:5][::-1]

class detailView(DetailView):
    template_name = 'polls/detail.html'
    model = question
    context_object_name = 'poll'

class resultsView(DetailView):
    template_name = 'polls/results.html'
    model = question
    context_object_name = 'poll'


def vote(request, pk):
    # return HttpResponse(f'You\'re voting on poll number {pk}')

    q = get_object_or_404(question, id=pk)
    try:
        selected_choice = q.choice_set.all().get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'polls/vote.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', kwargs={'pk': q.id}))
    
    return render(request, 'polls/vote.html', context={'question': q})
