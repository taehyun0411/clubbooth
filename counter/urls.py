from django.urls import path, include
from counter.views import show_counter,increment_counter,done_counter
urlpatterns = [
    path("",show_counter, name="show_counter"),
    path("increment_counter/", increment_counter ,name="increment_counter"),
    path("done_counter/",done_counter ,name="done_counter"),
]