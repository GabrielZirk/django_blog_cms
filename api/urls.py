from api import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPostApiView.as_view(), name="api_view")
]