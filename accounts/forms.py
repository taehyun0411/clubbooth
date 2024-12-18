from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_id']

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not user_id.isdigit() or len(user_id) != 5:
            raise forms.ValidationError("아이디는 5자리 숫자여야 합니다.")
        return user_id
