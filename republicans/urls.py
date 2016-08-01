from django.conf.urls import url

from republicans.views import (
    SenatorList, RepresentativeList
)

urlpatterns = [
    url(r'^senators/$',
        SenatorList.as_view(),
        name='senator_list'),
    url(r'^representatives/$',
        RepresentativeList.as_view(),
        name='representative_list'),
]