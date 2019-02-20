from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProfileView
from RestApp.views import postlist

urlpatterns = [
    url(r'^profile/', ProfileView.as_view(),name="profile"),
    url(r'^post/', postlist.as_view(),name="post"),
]

url_patterns = format_suffix_patterns(urlpatterns)
