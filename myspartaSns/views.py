from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POSt.get('password',None)
        password2 = request.POSt.get('password2',None)
        bio = request.POSt.get('bio',None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            new_user.save()

        return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session('user') = me.username
            return HttpResponse("로그인 성공!")
        else:
            return redirect('/sign-in/')

    elif request.method == 'GET':
        return render(request, 'user/signin.html')