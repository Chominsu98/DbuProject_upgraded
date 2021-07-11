"""dbuchecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

import showing_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',showing_app.views.login_render,name="login_render"),
    path('login/',showing_app.views.login,name="login"),
    path('logout/',showing_app.views.logout,name="logout"),
    path('new/',showing_app.views.select,name='select'),
    path('home/',showing_app.views.home_UI,name='home'),
    path('qrcode/',showing_app.views.camera_exam,name='camera_exam'),
    path('qrcode/popup',showing_app.views.camera_data_pop,name='camera_data_pop'),
    
    
]
