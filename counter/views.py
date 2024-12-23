from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Counter
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # 메시지 프레임워크 추가
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
import base64
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()
def login_view그레이스(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login그레이스.html')
    return render(request, 'accounts/login그레이스.html')
def login_view뉴턴(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login뉴턴.html')
    return render(request, 'accounts/login뉴턴.html')

def login_view늘품(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login늘품.html')
    return render(request, 'accounts/login늘품.html')

def login_view데이터무제한(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login데이터무제한.html')
    return render(request, 'accounts/login데이터무제한.html')

def login_view데카르트(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login데카르트.html')
    return render(request, 'accounts/login데카르트.html')

def login_view도담(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login도담.html')
    return render(request, 'accounts/login도담.html')

def login_view디세뇨(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login디세뇨.html')
    return render(request, 'accounts/login디세뇨.html')

def login_view디아리오(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login디아리오.html')
    return render(request, 'accounts/login디아리오.html')

def login_view라온제나(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login라온제나.html')
    return render(request, 'accounts/login라온제나.html')

def login_view리사(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login리사.html')
    return render(request, 'accounts/login리사.html')

def login_view매드매쓰(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login매드매쓰.html')
    return render(request, 'accounts/login매드매쓰.html')

def login_view메이키스(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login메이키스.html')
    return render(request, 'accounts/login메이키스.html')

def login_view빌리네어(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login빌리네어.html')
    return render(request, 'accounts/login빌리네어.html')

def login_view세미콜론(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login세미콜론.html')
    return render(request, 'accounts/login세미콜론.html')

def login_view소솜(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login소솜.html')
    return render(request, 'accounts/login소솜.html')

def login_view수학에복종(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login수학에복종.html')
    return render(request, 'accounts/login수학에복종.html')
def login_view실험의숲(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login실험의숲.html')
    return render(request, 'accounts/login실험의숲.html')
def login_view심쿵(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login심쿵.html')
    return render(request, 'accounts/login심쿵.html')

def login_view아리솔(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login아리솔.html')
    return render(request, 'accounts/login아리솔.html')

def login_view아페토(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login아페토.html')
    return render(request, 'accounts/login아페토.html')

def login_view에스쿱(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login에스쿱.html')
    return render(request, 'accounts/login에스쿱.html')

def login_view에어로테크(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login에어로테크.html')
    return render(request, 'accounts/login에어로테크.html')

def login_view엘리제(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login엘리제.html')
    return render(request, 'accounts/login엘리제.html')
def login_view온에어(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login온에어.html')
    return render(request, 'accounts/login온에어.html')
def login_view폴리머(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login폴리머.html')
    return render(request, 'accounts/login폴리머.html')
def login_view피지카스트로(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login피지카스트로.html')
    return render(request, 'accounts/login피지카스트로.html')
def login_view하람(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 홈 페이지로 리디렉션
        else:
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login하람.html')
    return render(request, 'accounts/login하람.html')





@login_required
def show_counter그레이스 (request):
    return render(request, 'counter/그레이스getNFC.html')
def show_counter뉴턴 (request):
    return render(request, 'counter/뉴턴getNFC.html')
def show_counter늘품 (request):
    return render(request, 'counter/늘품getNFC.html')
def show_counter데이터무제한 (request):
    return render(request, 'counter/데이터무제한getNFC.html')
def show_counter데카르트 (request):
    return render(request, 'counter/데카르트getNFC.html')
def show_counter도담 (request):
    return render(request, 'counter/도담getNFC.html')
def show_counter디세뇨 (request):
    return render(request, 'counter/디세뇨getNFC.html')
def show_counter디아리오 (request):
    return render(request, 'counter/디아리오getNFC.html')
def show_counter라온제나 (request):
    return render(request, 'counter/라온제나getNFC.html')
def show_counter리사 (request):
    return render(request, 'counter/리사getNFC.html')
def show_counter매드매쓰 (request):
    return render(request, 'counter/매드매쓰getNFC.html')
def show_counter메이키스 (request):
    return render(request, 'counter/메이키스getNFC.html')
def show_counter빌리네어 (request):
    return render(request, 'counter/빌리네어getNFC.html')
def show_counter세미콜론 (request):
    return render(request, 'counter/세미콜론getNFC.html')
def show_counter소솜 (request):
    return render(request, 'counter/소솜getNFC.html')
def show_counter수학에복종 (request):
    return render(request, 'counter/수학에복종getNFC.html')
def show_counter실험의숲 (request):
    return render(request, 'counter/실험의숲getNFC.html')
def show_counter심쿵 (request):
    return render(request, 'counter/심쿵getNFC.html')
def show_counter아리솔 (request):
    return render(request, 'counter/아리솔getNFC.html')
def show_counter아페토 (request):
    return render(request, 'counter/아페토getNFC.html')
def show_counter에스쿱 (request):
    return render(request, 'counter/에스쿱getNFC.html')
def show_counter에어로테크 (request):
    return render(request, 'counter/에어로테크getNFC.html')
def show_counter엘리제 (request):
    return render(request, 'counter/엘리제getNFC.html')
def show_counter온에어 (request):
    return render(request, 'counter/온에어getNFC.html')
def show_counter폴리머 (request):
    return render(request, 'counter/폴리머getNFC.html')
def show_counter피지카스트로 (request):
    return render(request, 'counter/피지카스트로getNFC.html')
def show_counter하람 (request):
    return render(request, 'counter/하람getNFC.html')
@login_required
def increment_counter그레이스(request): # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value그레이스) >= 1:
        return redirect('done_counter그레이스')
    elif user.value그레이스 == 0:
        user.value그레이스 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트
@login_required
def increment_counter뉴턴(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value뉴턴) >= 1:
        return redirect('done_counter뉴턴')
    elif user.value뉴턴 == 0:
        user.value뉴턴 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter늘품(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value늘품) >= 1:
        return redirect('done_counter늘품')
    elif user.value늘품 == 0:
        user.value늘품 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter데이터무제한(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value데이터무제한) >= 1:
        return redirect('done_counter데이터무제한')
    elif user.value데이터무제한 == 0:
        user.value데이터무제한 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter데카르트(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value데카르트) >= 1:
        return redirect('done_counter데카르트')
    elif user.value데카르트 == 0:
        user.value데카르트 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter도담(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value도담) >= 1:
        return redirect('done_counter도담')
    elif user.value도담 == 0:
        user.value도담 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter디세뇨(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value디세뇨) >= 1:
        return redirect('done_counter디세뇨')
    elif user.value디세뇨 == 0:
        user.value디세뇨 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter디아리오(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value디아리오) >= 1:
        return redirect('done_counter디아리오')
    elif user.value디아리오 == 0:
        user.value디아리오 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter라온제나(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value라온제나) >= 1:
        return redirect('done_counter라온제나')
    elif user.value라온제나 == 0:
        user.value라온제나 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter리사(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value리사) >= 1:
        return redirect('done_counter리사')
    elif user.value리사 == 0:
        user.value리사 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter매드매쓰(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value매드매쓰) >= 1:
        return redirect('done_counter매드매쓰')
    elif user.value매드매쓰 == 0:
        user.value매드매쓰 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter메이키스(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value메이키스) >= 1:
        return redirect('done_counter메이키스')
    elif user.value메이키스 == 0:
        user.value메이키스 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter빌리네어(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value빌리네어) >= 1:
        return redirect('done_counter빌리네어')
    elif user.value빌리네어 == 0:
        user.value빌리네어 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter세미콜론(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value세미콜론) >= 1:
        return redirect('done_counter세미콜론')
    elif user.value세미콜론 == 0:
        user.value세미콜론 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter소솜(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value소솜) >= 1:
        return redirect('done_counter소솜')
    elif user.value소솜 == 0:
        user.value소솜 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter수학에복종(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value수학에복종) >= 1:
        return redirect('done_counter수학에복종')
    elif user.value수학에복종 == 0:
        user.value수학에복종 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter실험의숲(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value실험의숲) >= 1:
        return redirect('done_counter실험의숲')
    elif user.value실험의숲 == 0:
        user.value실험의숲 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter심쿵(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value심쿵) >= 1:
        return redirect('done_counter심쿵')
    elif user.value심쿵 == 0:
        user.value심쿵 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter아리솔(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value아리솔) >= 1:
        return redirect('done_counter아리솔')
    elif user.value아리솔 == 0:
        user.value아리솔 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter아페토(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value아페토) >= 1:
        return redirect('done_counter아페토')
    elif user.value아페토 == 0:
        user.value아페토 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter에스쿱(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value에스쿱) >= 1:
        return redirect('done_counter에스쿱')
    elif user.value에스쿱 == 0:
        user.value에스쿱 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter에어로테크(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value에어로테크) >= 1:
        return redirect('done_counter에어로테크')
    elif user.value에어로테크 == 0:
        user.value에어로테크 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter엘리제(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value엘리제) >= 1:
        return redirect('done_counter엘리제')
    elif user.value엘리제 == 0:
        user.value엘리제 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter온에어(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value온에어) >= 1:
        return redirect('done_counter온에어')
    elif user.value온에어 == 0:
        user.value온에어 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter폴리머(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value폴리머) >= 1:
        return redirect('done_counter폴리머')
    elif user.value폴리머 == 0:
        user.value폴리머 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter피지카스트로(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value피지카스트로) >= 1:
        return redirect('done_counter피지카스트로')
    elif user.value피지카스트로 == 0:
        user.value피지카스트로 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

@login_required
def increment_counter하람(request):
    user, created = User.objects.get_or_create(id=1)  # 첫 번째 카운터 객체 가져오기 or 생성
    user = request.user
    if int(user.value하람) >= 1:
        return redirect('done_counter하람')
    elif user.value하람 == 0:
        user.value하람 += 1
        user.money += 500000# 값 1 증가
        user.save()  # 저장
        return redirect('alhome')  # 리다이렉트

def done_counter그레이스(request):
    return render(request, 'counter/그레이스doneNFC.html')
def done_counter뉴턴(request):
    return render(request, 'counter/뉴턴doneNFC.html')
def done_counter늘품(request):
    return render(request, 'counter/늘품doneNFC.html')
def done_counter데이터무제한(request):
    return render(request, 'counter/데이터무제한doneNFC.html')
def done_counter데카르트(request):
    return render(request, 'counter/데카르트doneNFC.html')
def done_counter도담(request):
    return render(request, 'counter/도담doneNFC.html')
def done_counter디세뇨(request):
    return render(request, 'counter/디세뇨doneNFC.html')
def done_counter디아리오(request):
    return render(request, 'counter/디아리오doneNFC.html')
def done_counter라온제나(request):
    return render(request, 'counter/라온제나doneNFC.html')
def done_counter리사(request):
    return render(request, 'counter/리사doneNFC.html')
def done_counter매드매쓰(request):
    return render(request, 'counter/매드매쓰doneNFC.html')
def done_counter메이키스(request):
    return render(request, 'counter/메이키스doneNFC.html')
def done_counter빌리네어(request):
    return render(request, 'counter/빌리네어doneNFC.html')
def done_counter세미콜론(request):
    return render(request, 'counter/세미콜론doneNFC.html')
def done_counter소솜(request):
    return render(request, 'counter/소솜doneNFC.html')
def done_counter수학에복종(request):
    return render(request, 'counter/수학에복종doneNFC.html')
def done_counter실험의숲(request):
    return render(request, 'counter/실험의숲doneNFC.html')
def done_counter심쿵(request):
    return render(request, 'counter/심쿵doneNFC.html')
def done_counter아리솔(request):
    return render(request, 'counter/아리솔doneNFC.html')
def done_counter아페토(request):
    return render(request, 'counter/아페토doneNFC.html')
def done_counter에스쿱(request):
    return render(request, 'counter/에스쿱doneNFC.html')
def done_counter에어로테크(request):
    return render(request, 'counter/에어로테크doneNFC.html')
def done_counter엘리제(request):
    return render(request, 'counter/엘리제doneNFC.html')
def done_counter온에어(request):
    return render(request, 'counter/온에어doneNFC.html')
def done_counter폴리머(request):
    return render(request, 'counter/폴리머doneNFC.html')
def done_counter피지카스트로(request):
    return render(request, 'counter/피지카스트로doneNFC.html')
def done_counter하람(request):
    return render(request, 'counter/하람doneNFC.html')

