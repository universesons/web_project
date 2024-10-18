# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse("Welcome to Banking System")
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer