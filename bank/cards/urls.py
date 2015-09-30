from django.conf.urls import url
from .views import CardCreate, CardDetail, CardUpdate, CardList

urlpatterns = [
    url(r'^add', CardCreate.as_view(), name='create_card'),
    url(r'^detail/(?P<pk>[-\w]+)/$', CardDetail.as_view(), name='card_detail'),
    url(r'^(?P<pk>[-\w]+)/$', CardUpdate.as_view(), name='card_detail'),
    url(r'^$', CardList.as_view(), name='card_list'),
]
