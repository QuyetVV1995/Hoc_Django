from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, sendEmail
# Create your views here.


def index(request):
    return HttpResponse('Xin chao')


def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})

def save_news(request):
    if request.method == 'POST':
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('luu OK')
        else:
            return HttpResponse('Khong luu duoc valid')
    else:
        HttpResponse('Khong phai post request')

def emailView(request):
    b =sendEmail()
    return  render(request, 'news/email.html', {'f': b})

def process(request):
    if request.method == 'POST':
        m = sendEmail(request.POST)
        if m.is_valid():
            tieude = m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            noidung = m.cleaned_data['content']
            email = m.cleaned_data['email']
            context = {'td':tieude, 'cc': cc, 'b': noidung, 'd':email}
            # context2 = { 'email_data': m}
            return render(request,'news/print_email.html', context)
        else:
            return HttpResponse('form not validate')
    else:
        return HttpResponse('Khong phai POST method')