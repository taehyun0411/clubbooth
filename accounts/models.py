from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
    money = models.BigIntegerField(default=1000000)  # 돈 속성 (정수 타입)
    stocks = JSONField(default=dict)  # 주식 정보 (JSON 형태)




    is_active = models.BooleanField(default=True)  # 유저 활성/비활성
    is_staff = models.BooleanField(default=False)  # 스태프 권한 여부

    objects = UserManager()  # 커스텀 UserManager 사용

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []  # 필수 필드 없음



    def __str__(self):
        return self.user_id

    # 잔액 업데이트 메서드 (정수로 처리)
    def update_money(self, amount: int):
        """
        유저의 잔액을 업데이트합니다.
        `amount`는 정수 값이어야 하며, 양수는 입금, 음수는 출금입니다.
        """
        if self.money + amount < 0:
            raise ValueError("잔액이 부족합니다.")
        self.money += amount
        self.save()


class Stock(models.Model):
    name = models.CharField(max_length=100)
    current_price = models.IntegerField(default=1000)  # 정수 값으로 주식 가격 관리
    change_list = models.JSONField(default=list)  # 가격 변동 기록
    change_history = models.JSONField(default=list)

    def update_price(self):
        if not self.change_list:
            print(f"[WARN] {self.name}: change_list가 비어 있습니다.")
            self.reset_change_list()  # 비어 있는 경우 초기화
            return

        try:
            # 현재 적용된 변동 값의 개수
            applied_changes = len(self.change_history)

            # 순환 인덱스 계산: 리스트가 끝나면 처음으로 돌아감
            change_index = applied_changes % len(self.change_list)
            change = int(self.change_list[change_index])  # 현재 변동 값을 순환적으로 가져옴

            # 현재 가격 업데이트
            self.current_price = int(self.current_price * (1 + change / 100))

            # 변화 기록 추가
            if self.change_history is None:
                self.change_history = []
            self.change_history.append(change)  # 변동 기록 추가

            # DB 저장
            self.save()

            # 로그 출력
            print(
                f"[UPDATE] {self.name}: Current Price Updated to {self.current_price}, Applied Change: {change}%, Next Index: {change_index + 1}")

        except Exception as e:
            # 예외 처리
            print(f"[ERROR] {self.name}: {e}")

    def reset_change_list(self):
        """
        change_list 초기화
        """
        self.change_list = [5, -3, 2, -1, 1]  # 초기 변동 값 설정 (정수로)
        self.change_history = []  # 변화 기록 초기화
        self.save()
        print(f"[RESET] {self.name}: change_list와 change_history를 초기화했습니다.")


# 사용자별 보유 주식
class UserStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    average_price = models.IntegerField(default=0)  # 평균 매입 가격 (정수 값으로 처리)
class Article(models.Model):
    article = models.CharField(max_length=200)