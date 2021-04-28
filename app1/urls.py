from django.conf.urls import url
from django.urls import path
from . import views

app_name="app1" #引入命名空间、命名空间的名字最好和app的名字相同

urlpatterns = [

    url(r'^user/(.+)/$', views.user,name="user"),

    url(r'^goods/(.+)/$', views.goods,name="goods"),
    path('welcome/',views.welcome,name='welcome'),
]