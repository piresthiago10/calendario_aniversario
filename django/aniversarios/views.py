from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from aniversarios.models import Aniversario
from aniversarios.serializer import AniversarioSerializer


class AniversarioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os aniversários"""
    queryset = Aniversario.objects.all()
    serializer_class = AniversarioSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
