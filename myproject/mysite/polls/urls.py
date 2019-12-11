from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name='detail_view'),
    path('list/', views.viewList, name='view_list'),
    path('<int:question_id>', views.vote, name='vote'),
    path('', views.index, name='index'),    # dky duong dan
]