from rest_framework import serializers
from .models import Program, Week, Page


class PageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Page
        fields = ('id', 'name', 'complete', 'audio', 'video', 'article', 'question', 'form', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class WeekSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Week
        fields = ('id', 'name', 'pages', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    # def validate_pages(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Week must have 2 or more pages")
    #     return value

class ProgramSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Program
        fields = ('id', 'name', 'description', 'weeks', 'image', 'progress', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
