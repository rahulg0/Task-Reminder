"""task_rem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from cv2 import matMulDeriv
from django.contrib import admin
from django.urls import path
from login.views import login_action
from signup.views import signup_action
from create.views import create_action

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , login_action , name='login' ),
    path('login/' , login_action , name='login' ),
    path('signup/' , signup_action , name='signup' ),
    path('create/' , create_action , name='create'),
    path('dashboard/' , login_action , name='dashboard')
]
