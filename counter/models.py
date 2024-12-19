from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Counter(models.Model):
    value = models.PositiveIntegerField(default=0)  # 초기값 0

    def __str__(self):
        return f"Counter: {self.value}"
