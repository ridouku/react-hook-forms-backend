from django.test import TestCase

from my_awesome_api.serializers import PersonSerializer, PetsSerializer
from my_awesome_api.tests.factory import PersonModelFactory, PetModelFactory


class TestPersonSerializer(TestCase):

    # should test person model serialization
    def test_serialize_model(self):
        person = PersonModelFactory.create()
        serializer = PersonSerializer(person)
        self.assertNotEqual(hasattr(serializer.data, "id"), None)
        self.assertNotEqual(hasattr(serializer.data, "name"), None)
        self.assertNotEqual(hasattr(serializer.data, "birth_year"), None)
        self.assertNotEqual(hasattr(serializer.data, "identification"), None)


class TestPetSerializer(TestCase):

    # should test pet model serialization
    def test_serialize_model(self):
        pet = PetModelFactory.create()
        serializer = PetsSerializer(pet)
        self.assertNotEqual(hasattr(serializer.data, "id"), None)
        self.assertNotEqual(hasattr(serializer.data, "name"), None)
        self.assertNotEqual(hasattr(serializer.data, "owner"), None)
        self.assertNotEqual(hasattr(serializer.data, "age"), None)
