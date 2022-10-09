import django_filters.rest_framework
from rest_framework import generics
from vps.serializers import VpsDetailSerializer, VpsListSerializer
from vps.models import Vps


class VpsCreateView(generics.CreateAPIView):
    serializer_class = VpsDetailSerializer


class VpsListView(generics.ListAPIView):
    serializer_class = VpsListSerializer
    queryset = Vps.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['cpu', 'ram', 'hdd', 'status']


class VpsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VpsDetailSerializer
    queryset = Vps.objects.all()
