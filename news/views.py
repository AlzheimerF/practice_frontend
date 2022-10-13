from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializers


@api_view(['GET'])
def list_news(request):
    news = News.objects.all()
    serializer = NewsSerializers(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_news(request, id):
    news = News.objects.get(id=id)
    if news:
        serializer = NewsSerializers(news)
        return Response(serializer.data)

@api_view(['POST'])
def create_news(request):
    serializer = NewsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'Object': 'Created!'})

@api_view(['POST'])
def update_news(request, id):
    news = News.objects.get(id=id)
    serializer = NewsSerializers(instance=news, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_news(request, id):
    news = News.objects.get(id=id)
    if news:
        news.delete()
    return Response({'Object': 'Deleted!'})
