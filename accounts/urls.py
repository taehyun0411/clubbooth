from django.urls import path
from . import views

urlpatterns = [
    path('signup.html/', views.signup_view, name='signup'),
    path('login.html/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('alhome/', views.alhome, name='alhome'),
    path('buy/<int:stock_id>/', views.buy_stock, name='buy_stock'),
    path('sell/<int:stock_id>/', views.sell_stock, name='sell_stock'),
    path('stocks/buy/<int:stock_id>/', views.buy_stock_page, name='buy_stock_page'),  # 매수 페이지
    path('stocks/sell/<int:stock_id>/', views.sell_stock_page, name='sell_stock_page'),
    path('stocks/list/', views.stock_list_page, name='stock_list_page'),
    path('logout/', views.logout_view, name='logout'),

]