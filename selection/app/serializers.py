from rest_framework import serializers
from app.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'id',
            'name',
            'fees',
            'minimum_balance',
            'automated',
            'advisor',
            'ease_of_use'
        )