
from django.urls import path, include
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add_post'),
    path('save/', views.save_news, name='save'),
    path('email/', views.emailView, name='email'),
    path('process', views.process, name='process'),
]
