from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionDetail.as_view(), name='question_detail'),
]