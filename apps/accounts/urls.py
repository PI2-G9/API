# backend/server/apps/accounts/urls.py file

from django.conf.urls import url, include
from django.urls import path
from apps.accounts.views import UserProfileListCreateView

accounts_urlpatterns = [
    url(r'^accounts/', include('djoser.urls')),
    url(r'^accounts/', include('djoser.urls.authtoken')),
    path("accounts/all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
]
