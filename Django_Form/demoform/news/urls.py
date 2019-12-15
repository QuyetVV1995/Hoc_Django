
from django.urls import path, include
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('save/', views.ClassSaveNew.as_view(), name='save'),
    path('email/', views.emailView, name='email'),
    path('process', views.process, name='process'),
]
