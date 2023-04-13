from django.http import HttpResponse
from django.views.generic import View, TemplateView
import requests


class HomeView(TemplateView):
    template_name = "index.html"


class GraphChartView(TemplateView):
    template_name = "chart.html"


class JokesView(TemplateView):
    template_name = "jokes.html"

    # def get_context_data(self, **kwargs):
    #     context = super(JokesView, self).get_context_data(**kwargs)
    #     url = 'https://api.chucknorris.io/jokes/random'
    #     response = requests.get(url).json()
    #     joke = response['value']
    #     context['text'] = joke
    #     return context
