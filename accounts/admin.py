from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'money', 'is_active', 'is_staff')