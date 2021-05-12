from django.urls import path
from .views import ProfileList

app_name = 'events'

urlpatterns = [
    path('', ProfileList.as_view(), name='profilelistcreate')

]
