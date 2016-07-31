from django.conf.urls import url

from republicans.views import (
    SenatorList
)

urlpatterns = [
    url(r'^senators/$',
        SenatorList.as_view(),
        name='senator_list'),
]