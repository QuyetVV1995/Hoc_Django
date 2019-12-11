from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def index(request):         # dinh nghia ham
    myname = "Vu Van Quyet";
    list_item = ['Xe may', 'Dien thoai', 'laptop']
    return render(request,"polls/index.html",{"v_name": myname, "v_item":list_item});
