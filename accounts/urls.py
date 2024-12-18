from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('alhome/', views.profile_view, name='alhome'),
    path('profile/', views.profile, name='profile')
]