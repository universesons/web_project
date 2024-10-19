#这个文件作用是定义用户模型和银行账户模型

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager  # 导入AbstractUser和BaseUserManager,BaseUserManager是用于创建用户的管理器,AbstractUser是用于创建用户的模型类

#这里创建了一个自定义的用户管理器CustomUserManager，用于创建用户
class CustomUserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
#**extra_fields是用于创建用户时传入额外字段的，如email、first_name、last_name等
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username,password,**extra_fields)

# 这里创建了一个自定义的用户模型CustomUser，继承了AbstractUser
class CustomUser(AbstractUser):
    username = models.CharField(max_length=30,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
       # 指定用户名作为唯一标识
    def __str__(self):           # 返回用户名
        return self.username

class BankAccount(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) # 这里的OneToOneField表示一个用户只能对应一个银行账户
    # password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) # 余额为10位整数，2位小数
    account_number = models.CharField(max_length=20, unique=True) # 银行账号

    def __str__(self):
        return f"{self.user.username}的银行账户"
    
    

