from django.urls import path
from api import views

urlpatterns = [
    path("", views.check_answer, name="check_answer"),
]