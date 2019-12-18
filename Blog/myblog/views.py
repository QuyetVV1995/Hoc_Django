from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')    #Bai viet co trang thai public, va bai viet moi nhat se o tren cung
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




