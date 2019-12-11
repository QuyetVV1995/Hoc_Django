from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('list/', views.viewList, name='view_list'),
    path('', views.index, name='index'),    # dky duong dan
]