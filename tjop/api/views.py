from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import filters


from .models import HexValues, PicInfo
from .serializers import HexValuesSer, PicInfoSeri


class hex_values(ListAPIView):
    queryset = HexValues.objects.all()
    serializer_class = HexValuesSer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = [
        'color',
        'hex'
    ]
    ordering_fields = [
        'color',
    ]
    search_fields = [
        'color',
    ]


class pic_info(ListAPIView):
    queryset = PicInfo.objects.all()
    serializer_class = PicInfoSeri
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = {
        'episode': ['exact', 'icontains'],
        'painting_index': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'painting_title': ['icontains', 'exact'],
        'season': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'episode_num': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'num_colors': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'air_date': ['lt', 'gt', 'lte', 'gte', 'exact'],
    }
    ordering_fields = [
        'episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]
    search_fields = [
        'episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]
