from django.db import models

# Create your models here.
from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=50)  # 주식 이름
    current_price = models.FloatField()  # 현재 가격
    price_history = models.JSONField(default=list)  # 과거 가격 기록 (그래프용)

    def __str__(self):
        return self.name