from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

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


class addPost(LoginRequiredMixin, View):
    login_url = '/login/'           # Yeu cau login

    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request,'Login/addpost.html', context)
    def post(self, request):
        f = PostForm(request.POST)      # Bat du lieu nhap vao Postform
        if not f.is_valid():
            return HttpResponse('Nhap sai du lieu')
        print(request.user.get_all_permissions())        # In ra ca quyen cua User
        if request.user.has_perm('Login.add_post'):     # cu phap: Login.add_post = name_app.permission_name_models
            f.save()        # Luu du lieu vao database
        else:
            return HttpResponse('No permisson add post')
        return HttpResponse('Luu du lieu thanh cong')