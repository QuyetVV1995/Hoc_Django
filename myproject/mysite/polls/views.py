from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):  # dinh nghia ham
    myname = "Vu Van Quyet";
    list_item = ['Xe may', 'Dien thoai', 'laptop']
    return render(request, "polls/index.html", {"v_name": myname, "v_item": list_item});


def viewList(request):
    v_listQuestion = Question.objects.all()
    context = {"listques": v_listQuestion}
    # return render(request, "polls/question_list","listques":v_listQuestion)
    return render(request, "polls/question_list.html", context)
