from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [

    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]