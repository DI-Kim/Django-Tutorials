from django.urls import path

from . import views

urlpatterns = [
    # /polls/로 왔을 경우 해당!
    path('', views.index, name='index'),# r'^$'가 장고2.0에선 ''로 대체가능

    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote')
]