from rest_framework import serializers

from petclub.models import Pet

from .models import Person

#Serializar es estandarizar, dejarlo en JSON
#Deserializar pasarlo nuevamente a python
class CustomPetSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    specie = serializers.CharField()

    class Meta:
        model = Pet

class CustomPersonSerializer(serializers.ModelSerializer):
    firs_name = serializers.CharField(required= True)
    last_name = serializers.CharField(required = True)
    rut = serializers.CharField(required = True)
    class Meta:
        model = Pet



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
            
        
class PetSerializer(serializers.ModelSerializer):

    owner = PersonSerializer()
    class Meta:
        model = Pet
        fields = [
            'id',
            'species',
            'name2',
            'age',
            'owner',
        ]
        






