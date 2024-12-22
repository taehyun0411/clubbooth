from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'home.html')
def explanation(request):
    return redirect('explanation')