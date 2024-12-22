from django.contrib import admin
from .models import Stock, UserStock, User


# StockAdmin 정의 (change_history 숨김 처리)
class StockAdmin(admin.ModelAdmin):
    exclude = ('change_history',)  # change_history 필드를 관리자 페이지에서 숨김


# 관리자에 등록
admin.site.register(Stock, StockAdmin)  # 커스텀 Admin 클래스 사용
admin.site.register(UserStock)  # 기본 설정
admin.site.register(User)  # 기본 설정
