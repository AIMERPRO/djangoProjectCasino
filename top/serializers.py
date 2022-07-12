from rest_framework import serializers

from .models import NameTop


class NameTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameTop
        fields = '__all__'