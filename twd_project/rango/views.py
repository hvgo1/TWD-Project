from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)
    #return HttpResponse("Rango says hey there world!")

def about(request):
    return HttpResponse("Rango says you are in about page!")
