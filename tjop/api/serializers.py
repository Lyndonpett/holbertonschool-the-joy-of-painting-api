from rest_framework import serializers
from . import models


class HexValuesSer(serializers.ModelSerializer):
    class Meta:
        model = models.HexValues
        fields = [
            'index',
            'color',
            'hex'
        ]


class PicInfoSeri(serializers.ModelSerializer):
    class Meta:
        model = models.PicInfo
        fields = [
            'index',
            'episode',
            'painting_index',
            'img_src',
            'painting_title',
            'season',
            'episode_num',
            'num_colors',
            'youtube_src',
            'air_date'
        ]
