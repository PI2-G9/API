from rest_framework.generics import (ListCreateAPIView)
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from apps.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventList(ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        page = self.request.query_params.get('page')
        if page is not None:
            page = int(page)
        first = 50 * (page - 1) if page else 0
        last = 50 * page - 1 if page else 49
        queryset = Event.objects.order_by('-id')[first:last]
        cpf = self.request.query_params.get('cpf')
        if cpf is not None:
            queryset = Event.objects.filter(user=cpf).order_by('-id')[first:last]
        return queryset
