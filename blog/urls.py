from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view()),
    path('compose', views.ComposeBlogPostView.as_view(), name='compose'),
    path('userposts/<slug:slug>', views.UserPostsView.as_view(), name='user_posts')
]