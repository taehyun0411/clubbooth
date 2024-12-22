import threading
from django.apps import AppConfig


class StocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # 중복 실행 및 초기화 방지 플래그
    update_running = False  # 실행 중 상태 플래그
    initialized = False  # 초기화 여부 플래그
    lock = threading.Lock()  # Lock 객체 생성 (중복 실행 방지)

    def ready(self):
        from .models import Stock  # 모델 import

        def update_stock():
            with StocksConfig.lock:  # Lock으로 동기화하여 중복 실행 방지
                if StocksConfig.update_running:
                    print("[update_stock] 이미 실행 중입니다. 중복 실행 방지.")
                    return

                StocksConfig.update_running = True  # 실행 플래그 설정

            print("[update_stock] 주식 데이터를 업데이트합니다.")  # 업데이트 시작 출력
            try:
                stocks = Stock.objects.all()  # 모든 주식 가져오기
                for stock in stocks:
                    print(f"[update_stock] Updating stock: {stock.name}")  # 각 주식 업데이트 시작
                    stock.update_price()  # Stock 모델의 update_price 호출
            except Exception as e:
                print(f"[update_stock] 오류 발생: {e}")
            finally:
                # 실행 완료 후 플래그 해제
                with StocksConfig.lock:
                    StocksConfig.update_running = False

            # 주기적으로 실행 (10초 후 다시 호출)
            threading.Timer(300, update_stock).start()

        # `ready`가 여러 번 호출되는 상황 방지 (초기화된 경우 실행 스킵)
        if not StocksConfig.initialized:
            StocksConfig.initialized = True
            print("[ready] StocksConfig 초기화 완료. 주식 업데이트 스케줄러 시작.")
            threading.Thread(target=update_stock, daemon=True).start()
