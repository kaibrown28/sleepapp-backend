from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import sleepDataSerializer
from .models import sleepData

class sleepDataList(generics.ListCreateAPIView):
    queryset = sleepData.objects.all().order_by('id') 
    serializer_class = sleepDataSerializer

class sleepDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = sleepData.objects.all().order_by('id')
    serializer_class = sleepDataSerializer

    #use order_by('-field') to order by desc