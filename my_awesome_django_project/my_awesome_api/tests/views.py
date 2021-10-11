from django_mock_queries.query import MockSet
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from my_awesome_api.models import Person
from my_awesome_api.serializers import PersonSerializer
from my_awesome_api.tests.factory import PersonModelFactory, PetModelFactory, create_person
from django.urls import reverse
from my_awesome_api.views import PersonViewSet, PetsViewSet
import mock


class TestPersonView(TestCase):

    def setUp(self) -> None:
        self.request_factory = APIRequestFactory()

    # should test get method
    def test_get_request(self):
        view = PersonViewSet.as_view(actions={'get': 'list'})
        query_set_mock = MockSet(
            PersonModelFactory.build(),
            PersonModelFactory.build(),
            PersonModelFactory.build()
        )
        query_set_mock.model = Person
        with mock.patch.object(PersonViewSet, "get_queryset", return_value=query_set_mock):
            request = self.request_factory.get(reverse('people'))
            response = view(request)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 3)

    # should test post method
    def test_post_request(self):
        view = PersonViewSet.as_view(actions={'post': 'create'})
        post_data = {'name': 'test', 'birth_year': '1995', 'identification': '123'}

        request = self.request_factory.post(reverse('people'), post_data)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)

    # should test post method, with wrong input data
    def test_post_wrong_request(self):
        view = PersonViewSet.as_view(actions={'post': 'create'})
        post_data = {'name': 'test'}

        request = self.request_factory.post(reverse('people'), post_data)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # should test delete method
    def test_delete_request(self):
        person = PersonModelFactory.build()
        url = reverse("people", args=[])
        view = PersonViewSet.as_view(actions={'delete': 'destroy'})

        with mock.patch.object(PersonViewSet, "get_object", return_value=person):
            request = self.request_factory.delete(url)
            response = view(request)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestPetView(TestCase):

    def setUp(self) -> None:
        self.request_factory = APIRequestFactory()

    # should test get method
    def test_get_request(self):
        view = PetsViewSet.as_view(actions={'get': 'list'})
        query_set_mock = MockSet(
            PetModelFactory.build(),
            PetModelFactory.build(),
            PetModelFactory.build()
        )
        query_set_mock.model = Person
        with mock.patch.object(PetsViewSet, "get_queryset", return_value=query_set_mock):
            request = self.request_factory.get(reverse('pet'))
            response = view(request)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 3)

    # should test post method
    def test_post_request(self):
        view = PetsViewSet.as_view(actions={'post': 'create'})
        person = create_person()
        post_data = {'name': 'test', 'species': 'lorem', 'age': 1, 'owner': person.id}

        request = self.request_factory.post(reverse('pet'), post_data)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)

    # should test post method, with wrong input data
    def test_post_wrong_request(self):
        view = PetsViewSet.as_view(actions={'post': 'create'})
        post_data = {'name': 'test', 'species': 'lorem', 'age': 1}

        request = self.request_factory.post(reverse('pet'), post_data)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # should test delete method
    def test_delete_request(self):
        pet = PetModelFactory.build()
        url = reverse("pet", args=[])
        view = PetsViewSet.as_view(actions={'delete': 'destroy'})

        with mock.patch.object(PetsViewSet, "get_object", return_value=pet):
            request = self.request_factory.delete(url)
            response = view(request)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
