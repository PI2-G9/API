# backend/server/apps/accounts/urls.py file

from django.conf.urls import url, include
from django.urls import path
from apps.accounts.views import UserProfileListCreateView

accounts_urlpatterns = [
    url(r'^api/v1/', include('djoser.urls')),
    url(r'^api/v1/', include('djoser.urls.authtoken')),
    path("api/v1/all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
]
