from django.urls import path, include

urlpatterns = [
    path('v1/', include('vps.api.v1.urls'))
]
