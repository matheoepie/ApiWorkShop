from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import SituationSerializer, UserMessageSerializer
from .models import Situation, UserMessage


class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all().order_by('id')
    serializer_class = UserMessageSerializer

    
class SituationViewSet(viewsets.ModelViewSet):
    queryset = Situation.objects.all().order_by('id')
    serializer_class = SituationSerializer