from rest_framework import serializers
from glass.models import Message

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message',)