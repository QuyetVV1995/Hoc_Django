from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('Hello')


class LoginClass(View):
    def get(self,request):
        return render(request, 'Login/login.html')

    def post(self,request):
        v_username = request.POST.get('tendangnhap')
        v_password = request.POST.get('matkhau')
        myuser = authenticate(username=v_username, password=v_password)
        if myuser is None:
                return HttpResponse('User khong ton tai')
        login(request, myuser)
        return render(request, 'Login/success.html')

class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('Vui long dang nhap')
        else:
            return HttpResponse('Day la ViewUser')