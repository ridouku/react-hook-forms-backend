from django.test import TestCase
from my_awesome_api.models import Person
from my_awesome_api.models import Pet
from my_awesome_api.tests.factory import create_person


def create_pet(name="Test", species="dog", owner=None, age=1):
    return Pet.objects.create(name=name, species=species, owner=owner, age=age)


class PersonTest(TestCase):

    # should test person object creation
    def test_whatever_creation(self):
        person = create_person()
        self.assertTrue(isinstance(person, Person))
        self.assertTrue(hasattr(person, "id"))


class PetsTest(TestCase):

    # should test pet object creation
    def test_whatever_creation(self):
        person = create_person()
        pet = create_pet(owner=person)
        self.assertTrue(isinstance(pet, Pet))
        self.assertTrue(hasattr(pet, "id"))
        self.assertEqual(pet.name, "Test")
