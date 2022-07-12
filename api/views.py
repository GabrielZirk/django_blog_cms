from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BlogPostSerializer
from blog.models import BlogPost
from rest_framework import status

# Create your views here.


class BlogPostApiView(APIView):
    '''
    Retrieve all blog entries or post a new one
    '''
    def get(self, request):
        all_posts = BlogPost.objects.all().order_by('-date')
        serializer = BlogPostSerializer(all_posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    