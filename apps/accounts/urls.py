from django.conf.urls import url, include

accounts_urlpatterns = [
    url(r'^api/accounts/', include('djoser.urls')),
    url(r'^api/accounts/', include('djoser.urls.authtoken')),
]
