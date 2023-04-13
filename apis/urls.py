from django.urls import path, include

urlpatterns = [
    path('v1/', include('apis.v1.urls')),
]
