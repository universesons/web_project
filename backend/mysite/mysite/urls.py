"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from banking.views import RegisterView

urlpatterns = [
    # path("banking/",include("banking.urls")),
    path("api/register/",RegisterView.as_view(),name="register"),  #as_view()用于将类视图转换为视图函数，为什么要转换为视图函数？因为类视图需要通过请求对象进行处理，而视图函数不需要。
    path("admin/", admin.site.urls),   
]
