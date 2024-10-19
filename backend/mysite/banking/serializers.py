# 序列化器的作用是将模型类转换为JSON格式，以便于前端进行处理
# 这里处理的是BankAccount模型类
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BankAccount,CustomUser
import random

class BankAccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True,style={'input_type':'password'})   #这两行作用是只允许在前端输入，不允许在后台查看
    
    class Meta:
        model = BankAccount
        fields = ['id','username','account_number', 'balance', 'password']
        read_only_fields = ['account_number','balance']
    # create方法的作用是创建一个新的银行账户
    def create(self, validated_data):
        username = validated_data.pop('username') # 将username从validated_data中弹出并赋值给username,validated_data是传入的参数
        password = validated_data.pop('password') # 将password从validated_data中弹出并赋值给password
        user = CustomUser.objects.create_user(username=username, password=password) # 创建一个新的User对象
        account_number = ''.join(random.choice('0123456789') for _ in range(10)) # 生成一个10位的随机数作为account_number
        bank_account = BankAccount.objects.create(
            user=user, 
            account_number=account_number, 
            # password=password,
            **validated_data
        ) # 创建一个新的BankAccount对象,最后的**validated_data是传入的参数
        return bank_account # 返回bank_account对象

    # 这个方法的作用是重写返回的JSON格式，将username显示为username
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['username'] = instance.user.username
        return data
