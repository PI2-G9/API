# backend/server/apps/accounts/urls.py file

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.accounts.views import UserProfileListCreateView, add_photo_user, success

accounts_urlpatterns = [
    url(r'^accounts/', include('djoser.urls')),
    url(r'^accounts/', include('djoser.urls.authtoken')),
    path("accounts/all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("accounts/add-photo", add_photo_user, name='image_upload'),
    path("acconts/success", success, name="success")
]
if settings.DEBUG:
    accounts_urlpatterns += static(settings.MEDIA_URL,
                                   accounts_urlpatterns=settings.MEDIA_ROOT)
