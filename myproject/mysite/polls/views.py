from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):  # dinh nghia ham
    myname = "Vu Van Quyet";
    list_item = ['Xe may', 'Dien thoai', 'laptop']
    return render(request, "polls/index.html", {"v_name": myname, "v_item": list_item});


def viewList(request):
    v_listQuestion = Question.objects.all()    #Lay tat ca doi tuong nen khi in ra can dung vong for
    #v_listQuestion = get_object_or_404(Question, pk=4)  # Lay 1 doi tuong nen khi in ra ko can dung vong for
    context = {"listques": v_listQuestion}
    return render(request, "polls/question_list.html", context)
