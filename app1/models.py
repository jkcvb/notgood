from django.db import models

# Create your models here.
from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash

# Create your models here.
class User_login(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户昵称', null=False)
    phone = models.CharField(max_length=15, unique=True, verbose_name='手机号', null=True,blank=True)
    password_hash = models.CharField(max_length=50, verbose_name='密码')
    def __str__(self):
        return self.name
    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段
    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值




class Goods(models.Model):
    goodsname=models.CharField(max_length=20,verbose_name='商品名称',null=False)
    price=models.IntegerField()
    goodsimg=models.ImageField()
    goodsdes=models.CharField(max_length=200)
    type=models.ForeignKey('Goodscategory',on_delete=models.CASCADE)
    def __str__(self):
        return self.goodsname
class Goodscategory(models.Model):
    category=models.CharField(max_length=20,verbose_name='商品种类')
    def __str__(self):
        return self.category

