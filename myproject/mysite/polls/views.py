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

def detailView(request, question_id):
    v_ques = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": v_ques})


def vote(request, question_id):
    v_ques = Question.objects.get(pk=question_id)
    try:
        duLieu = request.POST['choice']
        c = v_ques.choice_set.get(pk=duLieu)     # Lay cau tra loi cua cau hoi co pk = question_id
    except:
        HttpResponse('Error')
    c.vote += 1
    c.save()
    return render(request, 'polls/result.html',{'q': v_ques})


