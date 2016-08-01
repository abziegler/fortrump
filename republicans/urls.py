from django.conf.urls import url

from republicans.views import (
    SenatorList, RepresentativeList, senator_detail
)

urlpatterns = [
    url(r'^senators/$',
        SenatorList.as_view(),
        name='senator_list'),
    url(r'^senators/(?P<slug>[\w\-]+)/$',
        senator_detail,
        name='senator_detail'),
    url(r'^representatives/$',
        RepresentativeList.as_view(),
        name='representative_list'),
]