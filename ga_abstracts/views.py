from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'ga_abstracts/index.html')

def about(request):
    return render(request, 'ga_abstracts/about.html')

def blog(request):
    return render(request, 'ga_abstracts/blog.html')