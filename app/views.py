from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy


def home(request):

    #获取轮播图数据
    wheels = Wheel.objects.all()


    #获取导航数据
    navs = Nav.objects.all()

    #获取每日必购数据
    mustbuys = Mustbuy.objects.all()

    data = {
        "wheels":wheels,
        "navs":navs,
        "mustbuys":mustbuys,
    }
    return render(request,'home/home.html',context=data)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')