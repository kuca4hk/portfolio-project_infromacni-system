from rest_framework import serializers
from .models import Class, Student, StudentDetail, StudyField


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = (
            "name",

        )


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = '__all__'


class StudyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyField
        fields = '__all__'
