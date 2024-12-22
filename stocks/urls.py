from django.urls import path, include
from stocks.views import stock
urlpatterns = [
    path("", stock, name="stock"),
]