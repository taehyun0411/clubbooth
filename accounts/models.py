from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import JSONField


class UserManager(BaseUserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        if not user_id or len(user_id) != 5 or not user_id.isdigit():
            raise ValueError("User ID는 5자리 숫자여야 합니다.")
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=5, unique=True)  # 숫자 5자리
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # 돈 속성
    stocks = JSONField(default=dict)  # 주식 정보 (JSON 형태)

    is_active = models.BooleanField(default=True)  # 유저 활성/비활성
    is_staff = models.BooleanField(default=False)  # 스태프 권한 여부

    objects = UserManager()  # 커스텀 UserManager 사용

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []  # 필수 필드 없음

    def __str__(self):
        return self.user_id
