from django.shortcuts import render

# Create your views here.
# stock/views.py

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from accounts.models import User
from .models import Stock


@login_required
def buy_stock(request):
    if request.method == "POST":
        stock_name = request.POST.get('stock_name')
        amount = int(request.POST.get('amount'))

        stock = get_object_or_404(Stock, name=stock_name)
        user = request.user

        total_cost = stock.current_price * amount

        if user.money >= total_cost:
            user.money -= total_cost

            # 보유 주식 업데이트
            user_stock = user.stocks.get(stock_name, {'amount': 0, 'average_price': 0})
            previous_amount = user_stock['amount']
            previous_average = user_stock['average_price']

            new_average_price = (previous_average * previous_amount + total_cost) / (previous_amount + amount)
            user.stocks[stock_name] = {
                'amount': user_stock['amount'] + amount,
                'average_price': round(new_average_price, 2)
            }
            user.save()

            return JsonResponse({"status": "success", "message": f"{stock_name}를 {amount}주 매수했습니다."})
        else:
            return JsonResponse({"status": "error", "message": "잔액이 부족합니다."})

@login_required
def sell_stock(request):
    if request.method == "POST":
        stock_name = request.POST.get('stock_name')
        amount = int(request.POST.get('amount'))

        stock = get_object_or_404(Stock, name=stock_name)
        user = request.user

        user_stock = user.stocks.get(stock_name)

        if user_stock and user_stock['amount'] >= amount:
            total_revenue = stock.current_price * amount
            user.money += total_revenue

            user.stocks[stock_name]['amount'] -= amount

            # 주식을 모두 매도하면 기록 제거
            if user.stocks[stock_name]['amount'] == 0:
                del user.stocks[stock_name]

            user.save()

            return JsonResponse({"status": "success", "message": f"{stock_name}를 {amount}주 매도했습니다."})
        else:
            return JsonResponse({"status": "error", "message": "보유 수량이 부족합니다."})

def get_stock_performance(user):
    performance = {}
    from .models import Stock

    for stock_name, data in user.stocks.items():
        stock = Stock.objects.get(name=stock_name)
        current_price = stock.current_price
        average_price = data['average_price']
        profit_percentage = ((current_price - average_price) / average_price) * 100

        performance[stock_name] = {
            "amount": data['amount'],
            "current_price": current_price,
            "average_price": average_price,
            "profit_percentage": round(profit_percentage, 2)
        }
    return performance