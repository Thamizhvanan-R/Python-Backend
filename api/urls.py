from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView

urlpatterns = [
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^bucketlist/', CreateView.as_view(),name="create"),
]

url_patterns = format_suffix_patterns(urlpatterns)
