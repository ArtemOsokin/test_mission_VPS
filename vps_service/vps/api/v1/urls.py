from django.urls import path, include
from vps.api.v1.views import *


app_name = 'vps'
urlpatterns = [
    path('vps/create', VpsCreateView.as_view()),
    path('all/', VpsListView.as_view()),
    path('vps/detail/<uuid:pk>', VpsDetailView.as_view())
]