from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Card


class CardCreate(CreateView):
    model = Card
    fields = '__all__'


class CardDetail(DetailView):
    model = Card


class CardList(ListView):
    model = Card


class CardUpdate(UpdateView):
    model = Card
    fields = '__all__'
