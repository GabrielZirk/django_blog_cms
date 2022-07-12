from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BlogPostSerializer
from blog.models import BlogPost
from rest_framework import status, permissions, authentication, generics

# Create your views here.


class BlogPostApiView(generics.ListCreateAPIView):
    '''
    Retrieve all blog entries or post a new one.
    '''
    queryset = BlogPost.objects.all().order_by('-date')
    serializer_class = BlogPostSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    