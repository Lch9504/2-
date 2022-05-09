from django.urls import path

from accountapp import views
from accountapp.views import hello_world, hello_world_drf, member_register
from . import views

# views.py에서 만든 함수
urlpatterns = [
   path('hello_world/', hello_world),

   path('hello_world_drf/', hello_world_drf),

   path('member/', member_register),

   path('home/', views.home, name='home'), # views.py 에서 home 이라는 함수 임포트 후 name='home'으로 표현식 이름을 정해줌

   path('member_idcheck', views.member_idcheck, name='member_idcheck'),

]

