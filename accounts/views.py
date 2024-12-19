from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

User = get_user_model()
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('alhome')  # 홈 페이지로 리디렉션
        else:
            return render(request, 'accounts/login.html', {'error': '로그인 실패'})

    return render(request, 'accounts/login.html')
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            User.objects.create_user(user_id=username, password=password)
            return redirect('login')  # 로그인 페이지로 리디렉션
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다'})

    return render(request, 'accounts/signup.html')
@login_required
def profile_view(request):
    # 사용자 객체 가져오기
    user = request.user

    # 사용자와 관련된 데이터 예시
    money = getattr(user, "money", 0)  # money 필드는 모델에 따라 다를 수 있음
    stocks = getattr(user, "stocks", [])  # stocks 필드 예시

    # 사용자 정보를 템플릿으로 전달
    context = {
        'money': money,
        'stocks': stocks,
        'username': user.user_id,
    }
    return render(request, 'accounts/alhome.html', context)

def profile(request):
    if request.user.is_authenticated:
        username = request.user.user_id  # 현재 로그인된 사용자의 이름
    else:
        username = None
    return render(request, 'accounts/profile.html', {'user_id': username})
