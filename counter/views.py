from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
import counter
from .models import Counter


def show_counter(request):
    counter, created = Counter.objects.get_or_create(id=1)
    return render(request, 'counter/getNFC.html')



def increment_counter(request):
    counter, created = Counter.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    if counter.value >= 1:
        return redirect('done_counter')

    elif counter.value == 0:
        counter.value += 1  # 값 1 증가
        counter.save()  # 저장
        return redirect('index')  # 리다이렉트


def done_counter(request):
    return render(request,'counter/doneNFC.html')
