from rest_framework import serializers
from .models import Person, PersonDetail


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonDetailSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = PersonDetail
        fields = '__all__'


class PersonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonDetail
        fields = "__all__"
