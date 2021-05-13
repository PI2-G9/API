from django.urls import path
from .views import ProfileList, ProfileCreate, ProfilePhotoList

app_name = 'events'

urlpatterns = [
    path('', ProfileList.as_view(), name='profilelist'),
    path('create/', ProfileCreate.as_view(), name='profilecreate'),
    path('photos/', ProfilePhotoList.as_view(), name='profilephotolist')
]
