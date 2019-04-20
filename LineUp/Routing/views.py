from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    content = {
        'start': 'uw bothell', 
        'end': 'seattle',
    }
    # return HttpResponse("Hello World")
    
    return render(request, 'index.html', content)