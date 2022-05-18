from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def sign_up(request):
    context = {}
#요청이 post인지 확인
    if request.method == 'POST' :
#1. 요청받은 requeset에서 username이 존재하는 wl
#2. 요청받은 request에서 password가 존재하는 지
#3. 요청받은 request에서 password 와 password_check가 맞는 지
        kusername = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if kusername and password and password == password_check :
            try :
                new_user = User.objects.create_user( kusername, password )
                #세로운 유저 아이로 로그인
                auth.login(request, new_user)
                #리디렉트 블로그 홈 
                return redirect('blog_samples:home') 
            except:
                context['error'] = '이미 존재하는 아이디입니다.'
        else : 
            context['error'] = '아이디와 비밀번호를 잘못 입력하셨습니다.'
#조건이 맞지 않을 경우 에러메세지 컨텍스트에 담기 
    return render(request, 'my_accounts/sign_up.html', context)

def login(request) :
    if request.user.is_authenticated:
        return redirect ("blog_samples:home")

    context ={}
    if request.method == 'POST':
        #아이디 입력 받았는 지
        #비밀번호 입력 받았는 지 
        #비밀번호 체크 -- 필요한 함수
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username and password) :
            user = auth.authenticate(request,username = username,password = password)
        #   로그인 , 리디렉션
            if user :
                auth.login(request, user)
                return redirect('blog_samples:home')
        #context 에러 ㄴ메세지 담아주기
            else :
                context['error'] = '아이디와 비밀번호가 틀렸습니다.'
        else :
            context['error'] = '아이디와 비밀번호를 입력해주세요'
    return render(request, 'my_accounts/login.html',context)

def logout(request) :
    #요청이 Post 인지 확인
    #if request.method == "POST" :
        #로그아웃
    auth.logout(request)
    #리다이렉트 시켜주기 
    return redirect('blog_samples:home')

def naver_test (request) :
    return render (request, 'my_accounts/naver_test.html')                                                                                                                                                                     