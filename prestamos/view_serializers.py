from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Prestamo
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer