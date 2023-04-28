from django.shortcuts import render

from .models import Quiz


def index(request):
    quizes = Quiz.objects.all()
    return render(request, 'battles/index.html', {'quizes': quizes})
