import random
import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm, GeneratorForm
from .models import *


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        data = form.data.dict()
        data.pop('csrfmiddlewaretoken')
        for i in data.copy():
            if not data[i]:
                data.pop(i)

        cards = Card.objects.filter(**data)
    else:
        cards = Card.objects.all()
    form = SearchForm()
    return render(request, 'index.html', {'cards': cards, 'form': form})


def detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    history = History.objects.filter(card=card.pk)
    return render(request, 'detail.html', {'card': card, 'history': history})


def generator(request):
    if request.method == 'POST':
        form = GeneratorForm(request.POST)
        if form.is_valid():
            for i in range(form.cleaned_data['count']):
                if form.cleaned_data['period'] == '6 месяцев':
                    months = 6
                elif form.cleaned_data['period'] == '1 месяц':
                    months = 1
                else:
                    months = 12
                Card.objects.create(series=form.cleaned_data['series'],
                                    number=random.randint(0, 99999999999),
                                    date_end=timezone.now()+relativedelta(months=months),
                                    use_date=timezone.now(),
                                    summa=0,
                                    status='Active')
        form = GeneratorForm()
    else:
        form = GeneratorForm()
    return render(request, 'generator.html', {'form': form})


def delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('home')


def activate(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.status = 'Active'
    card.save()
    return render(request, 'detail.html', {'card': card, 'history': History.objects.filter(card=card.pk)})


def deactivate(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.status = 'Deactive'
    card.save()
    return render(request, 'detail.html', {'card': card, 'history': History.objects.filter(card=card.pk)})
