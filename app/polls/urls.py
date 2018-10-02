from django.urls import path

from . import views

urlpatterns = [
    # /polls/로 왔을 경우 해당!
    path('', views.index, name='index'),# r'^$'가 장고2.0에선 ''로 대체가능
]