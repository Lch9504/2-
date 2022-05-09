from django.forms import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from user.models import User

def joinform(request):
    return render(request, 'user/joinform.html')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def index(request):
    return render(request, 'user/index.html')

def main(request):
    return render(request, 'main/main.html')

def join(request):
    user = User()
    user.id = request.POST['id']
    user.password = request.POST['password']
    user.name = request.POST['name']
    user.gender = request.POST['gender']
    user.phone_num = request.POST['phone_num']
    user.save()

    return HttpResponseRedirect('./joinsuccess')

def loginform(request) :
    return render(request, 'user/loginform.html')

def login(request):
    results = User.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])

    # 로그인 실패
    if len(results)==0:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # 로그인 처리
    authUser = results[0]
    request.session['authUser'] = model_to_dict(authUser)

    return HttpResponseRedirect('./main')

def logout(request) :
    del request.session['authUser']
    return HttpResponseRedirect('./index')

def updateform(request) :
    user = User.objects.get(id=request.session['authUser']['id'])
    data = {
        'user':user
    }
    return render(request, 'user/updateform.html', data)

def update(request) :
    user = User.objects.get(id=request.session['authUser']['id'])
    user.name = request.POST['name']

    user.gender = request.POST['gender']
    if request.POST['password'] is not '':
        user.password = request.POST['password']
    user.save()

    request.session['authUser']['name']=user.name
    return HttpResponseRedirect('/user/updateform?result=success')

def checkID(request):
    try :
        user = User.objects.get(id=request.GET['id'])
    except Exception as e:
        user = None
    result = {
        'result' : 'success',
        # 'data' : model_todict(user) # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)