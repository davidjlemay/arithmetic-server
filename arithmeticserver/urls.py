"""arithmeticserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from operations.viewsets import QuestionViewSet
from users.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'operations', QuestionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    path(r'auth/register/', include('rest_auth.registration.urls')),
    path("",
        TemplateView.as_view(template_name="spa.html"),
        name="home",
    ),
]