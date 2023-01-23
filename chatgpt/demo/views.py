from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, get_resolver
from django.views import generic, View
from django.utils import timezone
from django.urls import resolve, Resolver404
from django.urls import include, path
from inspect import isclass

from .models import ChatGptQuery

from .forms import NewQueryForm

import requests
import json

APP_DIR = 'demo'

from django.urls import reverse

class HomeView(View):
    def get(self, request):
        urls = [reverse('demo:home'), reverse('demo:index'), reverse('demo:detail', kwargs={'pk': 1}), reverse('demo:new_query')]
        return render(request, 'demo/home.html', {'urls': urls})

class IndexView(generic.ListView):
    template_name = f'{APP_DIR}/index.html'
    context_object_name = 'all_queries'

    def get_queryset(self):
        """Previous 10 queries"""
        return ChatGptQuery.objects.order_by('id')[:10]
    
class DetailView(generic.DetailView):
    model = ChatGptQuery
    template_name = f'{APP_DIR}/detail.html'
    context_object_name = 'query'
    def get_queryset(self):
        """See query"""
        return ChatGptQuery.objects.filter(pk=self.kwargs['pk']).values()
    
def query_completions(prompt, api_key):
    url = "https://api.openai.com/v1/completions"
    model = "text-davinci-003"
    # Parameters for the prompt
    data = {
        "model": model, 
        "prompt": prompt, 
        "temperature": 0, 
        "max_tokens": 1000
    }

    response = requests.post(url, json=data, headers={'Authorization': f'Bearer {api_key}'})
    if response.status_code == 200:
        response_text = json.loads(response.text)
        return response_text["choices"][0]["text"].lstrip()

# Create
def new_query(request):
  if request.method == 'POST':
        form = NewQueryForm(request.POST)
        if form.is_valid():
          with(open('chatgpt/demo/api_key.txt', 'r')) as f:
              api_key = f.read()
          query = form.save(commit=False)
          prompt = form.cleaned_data["prompt"] 
          response = query_completions(prompt, api_key)
          form.save()
          return HttpResponseRedirect(reverse('demo:response', args=(query.id,), kwargs={'prompt' : prompt, 'response' : response}))
        else: 
          error = "Not valid form"
          return render(request, f'{APP_DIR}/new_query.html', {'error': error})
  elif request.method == 'GET':
      form = NewQueryForm()
      return render(request, f'{APP_DIR}/new_query.html', {'form': form})