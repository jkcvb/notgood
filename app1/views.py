from django.shortcuts import render

# Create your views here.
# coding=utf-8
from urllib.parse import urlsplit

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app1 import models

import json

from app1.models import Goods
from wtf.settings import MEDIA_URL


def user(req, p):
    if p == 'all':
        all = models.User_login.objects.all()
        dic = {}
        for i in all:
            dic[i.id] = {'name': i.name, 'phone': i.phone, 'password': i.password_hash}

        return JsonResponse(dic)
    else:
        try:
            user = models.User_login.objects.get(pk=p)
            dic = {}
            dic[user.id] = {'name': user.name, 'phone': user.phone, 'password': user.password_hash}

            # return HttpResponse(json.dumps(dic))
            return JsonResponse(dic)
        except:
            # return HttpResponse(json.dumps({'msg':'没有相关信息'}))
            return JsonResponse({'msg': '没有相关信息'})


def welcome(req):
    Goods.objects.filter(goodsname='苹果')
    img = Goods.objects.all()
    return render(req, 'welcome.html', {'img': img})

def index(req):
    img='曹贼.jpeg'
    return render(req,'index.html',{'img':img})

def goods(req, q):
    host = req.META['HTTP_HOST']
    if q == 'all':
        all = models.Goods.objects.all()
        dic = {}
        for i in all:
            dic[i.id] = {'id':i.id,'goodsname': i.goodsname, 'price': i.price, 'goodsdes': i.goodsdes,
                         'type': str(i.type.category), 'goodsimg': host + MEDIA_URL + str(i.goodsimg)}
        return JsonResponse(dic)
    else:
        try:
            i = models.Goods.objects.get(pk=q)
            dic = {}
            dic[user.id] = {'id':i.id,'goodsname': i.goodsname, 'price': i.price, 'goodsdes': i.goodsdes,
                            'type': str(i.type.category), 'goodsimg': host + MEDIA_URL + str(i.goodsimg)}

            # return HttpResponse(json.dumps(dic))
            return JsonResponse(dic)
        except:
            # return HttpResponse(json.dumps({'msg':'没有相关信息'}))
            return JsonResponse({'msg': '没有相关信息'})

