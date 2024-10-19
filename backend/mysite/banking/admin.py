# 这个文件是用于在Django的admin后台中注册BankAccount模型，并自定义显示的属性

from django.contrib import admin
from .models import BankAccount,CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff')

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'balance', 'customer_name')

    def customer_name(self, obj):
        return obj.user.username if obj.user else '' #作用是显示用户的用户名
    
    customer_name.short_description = 'Customer Name' #作用是显示表头的名称

