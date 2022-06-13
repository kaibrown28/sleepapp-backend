from rest_framework import serializers 
from .models import sleepData 

class sleepDataSerializer(serializers.ModelSerializer): 
    class Meta:
        model = sleepData 
        fields = ('id', 'name', 'age','date','hoursSlept','routine','sleepQuality',) 
