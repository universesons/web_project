# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse("Welcome to Banking System")
#详细说明视图文件作用，用于处理用户请求，并返回相应的响应。和路由的区别在于，视图文件是处理请求并返回响应，而路由是定义URL和视图函数之间的映射关系。
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  #作用是指定查询集，即要操作的模型类
    serializer_class = UserSerializer  #作用是指定序列化器，即如何序列化和反序列化模型类

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'msg':"User created successfully"}, status=status.HTTP_201_CREATED)