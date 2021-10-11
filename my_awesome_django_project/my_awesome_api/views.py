from rest_framework.viewsets import ModelViewSet, GenericViewSet
from my_awesome_api.serializers import PersonSerializer, PetsSerializer
from my_awesome_api.models import Person, Pet
from django.core.serializers import serialize
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PeopleViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, **kwargs):
        person_serializer = PersonSerializer(self.queryset, many=True)
        return JsonResponse(person_serializer.data, safe=False)

    def create(self, request, **kwargs):
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, **kwargs):
        person_id = kwargs['pk']
        person = Person.objects.filter(id=person_id)

        if person:
            person.delete()
            return JsonResponse({'message': '{} Person was deleted successfully!'.format(id)},
                                status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': "Person doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)


class PersonViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        person_id = kwargs['pk']
        person_model_data = Person.objects.filter(id=person_id)
        person_data_serialized = serialize("python", person_model_data)[0]

        if person_model_data:
            response = {
                'id': person_data_serialized['pk'],
                'name': person_data_serialized['fields']['name'],
                'birth_year': person_data_serialized['fields']['birth_year'],
                'identification': person_data_serialized['fields']['identification'],
                'lastname': person_data_serialized['fields']['lastname'],
            }
            return JsonResponse(response, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'message': "Person doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        person_id = kwargs['pk']
        instance = Person.objects.filter(id=person_id).first()
        if instance is None:
            return JsonResponse({'message': "Person doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

            logger.info(serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': "Data is not valid"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class PetsViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

    @action(methods=["get"], detail=True)
    def get_pets(self, request, **kwargs):
        pet_serializer = PetsSerializer(self.queryset, many=True)
        return JsonResponse(pet_serializer.data, safe=False)

    @action(methods=["post"], detail=False)
    def create_species(self, request, **kwargs):
        specie_data = JSONParser().parse(request)
        pet_serializer = PetsSerializer(data=specie_data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return JsonResponse(pet_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["delete"], detail=False)
    def delete_species(self, request, **kwargs):
        count = Pet.objects.all().delete()
        return JsonResponse({'message': '{} Specie was deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
