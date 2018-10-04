from django.urls import path, include

# from . import views
from .views import cbv, fbv as views

app_name = 'polls'

urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index'),
]
urlpatterns = [
    # /polls/로 왔을 경우 해당!
    path('', views.index, name='index'),# r'^$'가 장고2.0에선 ''로 대체가능

    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),

    #/polls/cbv로 시작하는 URL요청은
    # 위의 urlpatterns_cbv리스트 내의 내용에서 처리
    path('cbv/', include(urlpatterns_cbv)),
]