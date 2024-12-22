from django.urls import path, include
from main.views import index,explanation
urlpatterns = [
    path("", index, name="index"),
    path("explanation/",explanation,name="explanation"),
]