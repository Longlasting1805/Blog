from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .models import Blog, Comment
from .serialisers import BlogSerializer, commentSerializer


class BlogApiView(APIView):
    def get(self, request):
        articles = Blog.objects.all()
        serializer = BlogSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class blogDetailApi(APIView):
    def get_object(self, id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blog = self.get_object(id)
        blog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class commentView(APIView):
    def get(self, request):
        blog = Comment.objects.all()
        serializer = commentSerializer(blog, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = commentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

