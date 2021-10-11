from django.urls import include, path

from my_awesome_api.views import PetsViewSet, PersonViewSet, PeopleViewSet
from django.conf.urls import url
from rest_framework.routers import DefaultRouter


class CustomDefaultRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'


router = CustomDefaultRouter()

# router = DefaultRouter
router.register(r'people', PeopleViewSet)
router.register(r'person', PersonViewSet)
router.register(r'species', PetsViewSet)

people_request_methods = {'get': 'list', 'post': 'create', 'delete': 'destroy'}
person_request_methods = {'get': 'retrieve', 'patch': 'update'}

urlpatterns = [
    path('', include(router.urls)),
    url(r'^people$', PeopleViewSet.as_view(people_request_methods), name='people'),
    url(r'^person/(?P<pk>\d+)$', PersonViewSet.as_view(person_request_methods), name='person'),
    url(r'^pet$', PetsViewSet, name='pet'),
]
# /(?P<pk>[0-9]+)
