from django.shortcuts import render


def missions(request):
    return render(request, 'missions/missions.html')


def application(request):
    return render(request, 'missions/application.html')
# Create your views here.
