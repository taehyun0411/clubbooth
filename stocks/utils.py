# stock/utils.py
import random

# 주식 변동률 리스트 (-10% ~ +10%)
PRICE_VARIATION = [-0.1, -0.05, 0, 0.05, 0.1]  # 변동율 정의


def update_stock_prices():
    from .models import Stock
    stocks = Stock.objects.all()

    for stock in stocks:
        # 현재 가격의 변동률에 따라 새로운 가격 생성
        variation = random.choice(PRICE_VARIATION)  # 랜덤 선택
        new_price = round(stock.current_price * (1 + variation), 2)  # 새로운 가격
        stock.price_history.append(stock.current_price)  # 이전 가격 기록
        stock.current_price = new_price
        stock.save()
