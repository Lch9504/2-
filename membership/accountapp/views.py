
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserInfo
import json
# Create your views here.

# 기존 장고 방식
# def hello_world(request): # 요청을 받는 매개변수
#     return HttpResponse('Hello_world!')
def hello_world(request): # 요청을 받는 매개변수
    return render(request, 'accountapp/temp.html')

# DRF 방식으로
@api_view()
def hello_world_drf(request):
    return Response({'message': 'Hello, world!'})


def member_register(request) :
    return render(request, 'accountapp/member_register.html')


def home(request): # html 이동 함수 제작
    posts = UserInfo.objects.all()
    return render(request, 'accountapp/index.html', {"posts" : posts})

@csrf_exempt
def member_idcheck(request):
    context = {}

    memberid=request.GET['member_id'] # html 페이지에서 id가 member_id 인 태그 안에 값을 가져옴
    # UserInfo model.py 안에 있는 데이터 값중 html에서 가져온 member_id 와 테이블 컬럼 id를 비교
    rs = UserInfo.objects.filter(id=memberid)

    if(len(rs)) > 0:
        context['flag'] = '1'
        context['result_msg'] = '사용자 아이디 중복'
    else:
        context['flag'] = '0'
        context['result_msg'] = '사용 가능한 아이디 입니다.'

    return JsonResponse(context, content_type="application/json")

@csrf_exempt
def member_insert(request):
    context = {}
    id = request.GET['member_id']
    password = request.GET['member_pwd']
    name = request.GET['member_name']
    gender = request.GET['gender']
    phone_num = request.GET['member_phone']

    rs = UserInfo.objects.create(id=id,
                                 password=password,
                                 name=name,
                                 sex=gender,
                                 phone_num=phone_num)

    context['flag'] = '1'
    context['result_msg'] = '회원가입 되었습니다.<br>Home에서 로그인하세요.'

    return JsonResponse(context, content_type="application/json")


