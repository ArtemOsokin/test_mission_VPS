from typing import Type

from django.shortcuts import render
from rest_framework import generics
from vps.serializers import VpsDetailSerializer, VpsListSerializer
from vps.models import Vps


class VpsCreateView(generics.CreateAPIView):
    serializer_class = VpsDetailSerializer


class VpsListView(generics.ListAPIView):
    serializer_class = VpsListSerializer
    queryset = Vps.objects.all()
