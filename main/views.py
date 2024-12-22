from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')
def explanation(request):
    return render(request, 'explanation.html')