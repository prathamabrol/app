from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id","app_icon", "app_name", "app_link", "app_category", "sub_category", "points"]