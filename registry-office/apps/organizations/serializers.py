from rest_framework import serializers
from .models import Organization, VirtualOperation


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'osszName',
        )


class VirtualOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualOperation
        fields = '__all__'
