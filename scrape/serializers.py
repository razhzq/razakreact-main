from rest_framework import serializers
from .models import News, IndexPrice, NewsTech


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class IndexPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexPrice
        fields = '__all__'

class NewsTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTech
        fields = '__all__'
