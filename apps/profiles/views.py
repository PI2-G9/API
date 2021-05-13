from rest_framework.generics import (CreateAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.profiles.serializers import ProfileCreateSerializer, ProfileListSerializer, ProfilePhotoListSerializer
from .models import Profile


# Create your views here.

class ProfilePhotoList(ListAPIView):
    serializer_class = ProfilePhotoListSerializer
    queryset = Profile.objects.all()


class ProfileList(ListAPIView):
    serializer_class = ProfileListSerializer

    def get_queryset(self):
        page = self.request.query_params.get('page')
        if page is not None:
            page = int(page)
        first = 50 * (page - 1) if page else 0
        last = 50 * page - 1 if page else 49
        queryset = Profile.objects.order_by('created_at')[first:last][::-1]
        cpf = self.request.query_params.get('cpf')
        if cpf is not None:
            queryset = Profile.objects.filter(cpf=cpf)
        return queryset


class ProfileCreate(CreateAPIView):
    serializer_class = ProfileCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
