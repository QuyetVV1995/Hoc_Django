from .views import IndexClass, LoginClass, ViewUser
from django.urls import path


urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
    path('login/', LoginClass.as_view(), name='login'),
    path('viewuser', ViewUser.as_view(), name='viewuser'),

]
