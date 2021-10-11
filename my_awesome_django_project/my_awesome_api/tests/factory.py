import factory
from my_awesome_api.models import Person, Pet


class PersonModelFactory(factory.Factory):
    class Meta:
        model = Person

    id = factory.Faker('pyint', min_value=0, max_value=1000)
    name = factory.Faker('first_name')
    birth_year = factory.Faker('date_time')
    identification = factory.Faker('word')


class PetModelFactory(factory.Factory):
    class Meta:
        model = Pet

    id = factory.Faker('pyint', min_value=0, max_value=1000)
    name = factory.Faker('name')
    species = factory.Faker('word')
    age = factory.Faker('pyint', min_value=0, max_value=100)
    owner = factory.SubFactory(PersonModelFactory)


def create_person(name="Test", birth_year="12/12/1976", identification="123"):
    return Person.objects.create(name=name, birth_year=birth_year, identification=identification)
