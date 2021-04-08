from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Snippet
from .serializers import SnippetSerializer
from rest_api import serializers

# Create your views here.


@api_view(['GET', ])
def api_detail_view(request, id):
    try:
        snippet = Snippet.objects.get(pk=id)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)


@api_view(['POST', ])
def api_add_view(request):
    if request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def api_update_view(request, id):
    try:
        snippet = Snippet.objects.get(pk=id)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', ])
def api_delete_view(request, id):
    try:
        snippet = Snippet.objects.get(pk=id)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    if request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
