from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ViewUser(LoginRequiredMixin,View):    # Luu y nen de LoginRequiredMixin truoc View
    login_url = '/login/'
    def get(self, request):
        return HttpResponse('Day la ViewUser')


@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse('View Product')