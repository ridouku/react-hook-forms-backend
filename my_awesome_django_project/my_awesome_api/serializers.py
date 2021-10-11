from rest_framework import serializers

from my_awesome_api.models import Person, Pet


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'birth_year', 'identification', 'lastname')


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'species', 'age', 'owner')
