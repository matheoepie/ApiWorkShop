from rest_framework import serializers

from .models import Situation, UserMessage

class UserMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMessage
        fields = ('firstName', 'phone','email','age','description','createAt','bullyDate','anonym','isYou','situation')

class SituationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Situation
        fields = ('name','id')