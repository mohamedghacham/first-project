from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime




def vue_de_test(request):
    return HttpResponse("<h1>vue de test </h1>")


def bonjour(request):
    return render(request,"index.html",context={"date":datetime.today()})