from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, PersonDetail
from .serilazers import PersonSerializer, PersonDetailSerializer, PersonDetailSerializerAll
from rest_framework.response import Response
from unidecode import unidecode
from django.db.models.functions import Lower
# Create your views here.


# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


class PersonDetailViewSetAll(viewsets.ModelViewSet):
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializerAll


class PersonDetailViewSet(viewsets.ModelViewSet):
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializerAll

    def retrieve(self, request, *args, **kwargs):
        student_surname = kwargs.get('student_surname')
        student_surname_uni = unidecode(student_surname).lower()

        try:
            persondetails = PersonDetail.objects.all()
            filtered_persondetails = [p for p in persondetails if unidecode(p.lastName).lower() == student_surname_uni]
            serializer = PersonDetailSerializerAll(filtered_persondetails, many=True)
            return Response(serializer.data)
        except PersonDetail.DoesNotExist:
            return Response({'message': 'The class does not exist'}, status=404)
