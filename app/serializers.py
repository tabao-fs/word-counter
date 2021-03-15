from rest_framework import serializers

from .models import Website


class WebsiteCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for website create objects
    """
    class Meta:
        model = Website
        fields = ('id', 'word', 'url')
        read_only_fields = ('id',)


class WebsiteSerializer(serializers.ModelSerializer):
    """
    Serializer for website objects
    """
    class Meta:
        model = Website
        fields = ('id', 'word', 'url', 'count')
        read_only_fields = ('id',)
