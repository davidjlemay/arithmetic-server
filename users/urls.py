from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserDetail.as_view(), name='profile'),
]