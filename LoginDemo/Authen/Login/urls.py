from .views import IndexClass, LoginClass, ViewUser, view_product, addPost
from django.urls import path

app_name ='Login'
urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
    path('login/', LoginClass.as_view(), name='login'),
    path('viewuser/', ViewUser.as_view(), name='viewuser'),
    path('viewproduct/',view_product, name='viewproduct'),
    path('addpost/', addPost.as_view(), name='addpost'),


]
