from api import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.BlogPostApiView.as_view(), name="api_view"),
    path('auth/', obtain_auth_token)
]