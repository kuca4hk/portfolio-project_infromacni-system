from django.shortcuts import render
from rest_framework import viewsets
from .models import Organization, VirtualOperation
from .serializers import OrganizationSerializer, VirtualOperationSerializer
# Create your views here.


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class VirtualOperationViewSet(viewsets.ModelViewSet):
    queryset = VirtualOperation.objects.all()
    serializer_class = VirtualOperationSerializer
