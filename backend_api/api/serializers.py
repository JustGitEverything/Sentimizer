from rest_framework import serializers
from .models import DiaryEntry


class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ["pub_date", "title", "description", "happyness_value"]

#TODO Make User Serializer
