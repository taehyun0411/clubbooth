from wsgiref.util import request_uri

from django.contrib import messages  # 메시지 프레임워크 추가
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock, UserStock, Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.timezone import now
from datetime import timedelta
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
            messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            User.objects.create_user(user_id=username, password=password)
            messages.success(request, '회원가입이 완료되었습니다! 로그인해주세요.')
            return redirect('login')  # 로그인 페이지로 리디렉션
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')


def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def alhome(request):
    user = request.user
    user_stocks = UserStock.objects.filter(user=user)
    stocks = Stock.objects.all()
    user_stocks_dict = {user_stock.stock.id: user_stock for user_stock in user_stocks}

    # 수익률 계산
    for user_stock in user_stocks:
        user_stock.profit_percent = round(
            (user_stock.stock.current_price - user_stock.average_price) / user_stock.average_price * 100, 2
        )
    total_stock_value = sum(
        user_stock.quantity * user_stock.stock.current_price for user_stock in user_stocks
    )
    total_assets = user.money + total_stock_value

    context = {
        'user': user,
        'stocks': user_stocks,
        'all_stocks': stocks,
        'user_stocks_dict': user_stocks_dict,
        'total_assets': total_assets,
    }
    return render(request, "accounts/alhome.html", context)




# 매수
@login_required
def buy_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    user = request.user

    try:
        quantity = int(request.POST.get('quantity', 0))
        if quantity <= 0:
            raise ValueError("수량은 1개 이상이어야 합니다.")
    except ValueError:
        messages.error(request, "올바른 수량을 입력해주세요.")
        return redirect('alhome')

    total_price = stock.current_price * quantity

    if user.money < total_price:
        messages.error(request, "잔액이 부족합니다. 계좌 잔고를 확인해주세요.")
        return redirect('alhome')

    # 매수 처리
    user.money -= total_price
    user.save()

    # 보유 주식 업데이트
    user_stock, created = UserStock.objects.get_or_create(user=user, stock=stock)
    user_stock.average_price = (
                                       (user_stock.average_price * user_stock.quantity) + total_price
                               ) / (user_stock.quantity + quantity)
    user_stock.quantity += quantity
    user_stock.save()

    messages.success(request, f"{stock.name} 주식을 {quantity}주 매수했습니다!")
    return redirect('alhome')




# 매도
@login_required
def sell_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    user = request.user

    try:
        quantity = int(request.POST.get('quantity', 0))
        if quantity <= 0:
            raise ValueError("수량은 1개 이상이어야 합니다.")
    except ValueError:
        messages.error(request, "올바른 수량을 입력해주세요.")
        return redirect('alhome')

    user_stock = UserStock.objects.filter(user=user, stock=stock).first()
    if not user_stock or user_stock.quantity < quantity:
        messages.error(request, "보유한 주식보다 많은 수량을 매도할 수 없습니다.")
        return redirect('alhome')

    # 매도 처리
    total_sale = stock.current_price * quantity
    user.money += total_sale
    user.save()

    user_stock.quantity -= quantity
    user_stock.save()

    if user_stock.quantity == 0:
        user_stock.delete()  # 0개가 되면 삭제

    messages.success(request, f"{stock.name} 주식을 {quantity}주 매도했습니다!")
    return redirect('alhome')
def buy_stock_page(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)

    if request.method == 'POST':
        # 폼 데이터 처리
        quantity = int(request.POST.get('quantity', 0))
        total_price = stock.current_price * quantity

        # 사용자의 자금 확인
        if request.user.money < total_price:
            messages.error(request, "잔액이 부족합니다!")
            return redirect('buy_stock_page', stock_id=stock_id)

        # 잔액 차감 및 주식 구매 처리
        request.user.money -= total_price
        user_stock, created = UserStock.objects.get_or_create(user=request.user, stock=stock)
        user_stock.quantity += quantity
        user_stock.average_price = ((user_stock.average_price * (
                    user_stock.quantity - quantity)) + total_price) / user_stock.quantity
        user_stock.save()
        request.user.save()

        messages.success(request, f"{stock.name} 주식 {quantity}주를 구매했습니다!")
        return redirect('alhome')  # 포트폴리오로 리디렉션

    return render(request, 'buy.html', {'stock': stock})
def sell_stock_page(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    user_stock = get_object_or_404(UserStock, user=request.user, stock=stock)

    if request.method == 'POST':
        # 폼 데이터 처리
        quantity = int(request.POST.get('quantity', 0))

        if quantity > user_stock.quantity:
            messages.error(request, "보유 수량보다 많이 팔 수 없습니다!")
            return redirect('sell_stock_page', stock_id=stock_id)

        # 주식 판매 처리
        total_price = stock.current_price * quantity
        user_stock.quantity -= quantity
        if user_stock.quantity == 0:
            user_stock.delete()  # 보유 수량이 0이면 삭제
        else:
            user_stock.save()

        # 판매 대금 계좌 잔액에 추가
        request.user.money += total_price
        request.user.save()

        messages.success(request, f"{stock.name} 주식 {quantity}주를 매도했습니다!")
        return redirect('alhome')  # 포트폴리오로 리디렉션

    return render(request, 'sell.html', {'stock': stock, 'user_stock': user_stock})
@login_required
def stock_list_page(request):
    """
    주식 목록 페이지 - 모든 주식과 추가 매수 버튼 표시
    """
    stocks = Stock.objects.all()  # 모든 주식 불러오기
    stock_graphs = {}  # 각 주식의 그래프를 저장할 딕셔너리

    # 각 주식에 대해 그래프 생성

    context = {
        'stocks': stocks,
        'stock_graphs': stock_graphs,
    }
    return render(request, 'stocks/stock_list.html', context)
def logout_view(request):
    """
    사용자의 세션을 종료하여 로그아웃 실행
    """
    logout(request)  # 사용자 세션 만료
    messages.success(request, "성공적으로 로그아웃되었습니다.")  # 로그아웃 성공 메시지
    return redirect('login')

def article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'accounts/article.html', context)
@login_required
def ranking_view(request):
    users = User.objects.all()

    # 모든 유저에 대해 총자본 계산
    user_rankings = []
    for user in users:
        user_stocks = UserStock.objects.filter(user=user)
        total_stock_value = sum(
            user_stock.quantity * user_stock.stock.current_price for user_stock in user_stocks
        )
        total_assets = user.money + total_stock_value  # 총자본 계산
        user_rankings.append({'user': user, 'total_assets': total_assets})

    # 총자본 기준 내림차순 정렬
    user_rankings.sort(key=lambda x: x['total_assets'], reverse=True)

    # 상위 100위만 가져오기
    top_rankings = user_rankings[:100]

    context = {
        'user_rankings': top_rankings,
        'last_updated': now(),  # 마지막 갱신 시간 표시
    }
    return render(request, 'accounts/ranking.html', context)
