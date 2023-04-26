"""bank URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home),
    path('login/',views.login),
    path('select/',views.select),
    path('log/',views.log),
    path('refresh/',views.refresh),
    path('refresh1/',views.refresh1),
    path('recharge/',views.recharge),
    path('recharge1/',views.recharge1),
    path('user/',views.user),
    path('user1/',views.user1),
    path('name/',views.name),
    path('name1/',views.name1),

]
