from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

def index(request) :
    return render(request, 'index.html')

def months(request, month) : 
    month_list = []
    try :
        for m in range(1,13) :
            month_list.append(f'{m}월')
        return HttpResponse(month_list[month-1])
    except:   
        return HttpResponseNotFound('다시 입력해주세요.')

def details(request, name) :
  users = [
      {'name': 'hooni', 'email': 'hooni@naver.com', 'hobby': 'running'}, {'name': 'mina', 'email': 'mina@naver.com', 'hobby': 'dance'}, {'name': 'yami', 'email': 'yami@naver.com', 'hobby': 'reading'}, {'name': 'cool', 'email': 'cool@naver.com', 'hobby': 'surfing'}, {'name': 'jack', 'email': 'jack@naver.com', 'hobby': 'golf'}
    ]
  result = ""
  a_user = None
  for user in users :
    if user["name"] == name:
       #results += f"<h1>{user['name']}</h1><h2>{user['email']}</h2><h3>{user['hobby']}</h3>"
       #break
       a_user = user
       break
    return render(request, 'landing/users.html', a_user)

# def index(request) :
#     context = {
#         "weather_data" : {
#         "weather" : "아주 맑음",
#         "temperature" : "17도"
#         },
#         "members" : [
#         {'name': 'hooni', 'email': 'hooni@naver.com', 'hobby': 'running'},
#         {'name': 'janny', 'email': 'mina@naver.com', 'hobby': 'dance'}, 
#         {'name': 'jisu', 'email': 'yami@naver.com', 'hobby': 'reading'}, 
#         {'name': 'cool', 'email': 'cool@naver.com', 'hobby': 'surfing'},
#         {'name': 'jack', 'email': 'jack@naver.com', 'hobby': 'golf'}
#         ]
#     }


#     return render (request, "base.html", context)