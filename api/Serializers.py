



from rest_framework import serializers
from events.models import *
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['title','category']
