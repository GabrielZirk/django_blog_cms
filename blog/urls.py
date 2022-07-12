from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name='landing_page'),
    path('compose', views.ComposeBlogPostView.as_view(), name='compose'),
    path('userposts/<slug:author>', views.UserPostsView.as_view(), name='user_posts'),
    path('userposts/<slug:author>/<slug:slug>', views.DetailedPostView.as_view(), name='detailed_post'),
    path('edit/<slug:slug>', views.UpdatePostView.as_view(), name="update_post"),
    path('delete/<slug:slug>', views.DeletePostView.as_view(), name="delete_post")
]