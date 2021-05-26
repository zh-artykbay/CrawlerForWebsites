from rest_framework import serializers
from open_pages.models import Pages

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ('url', 'title')
