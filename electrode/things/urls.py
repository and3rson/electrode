from django.conf.urls import url
from rest_framework_nested.routers import SimpleRouter

from electrode.things import viewsets

router = SimpleRouter(trailing_slash=False)
router.register('domains/(?P<domain_id>[^/]+)/things', viewsets.ThingsViewSet, basename='thing')
router.register('domains/(?P<domain_id>[^/]+)/things/(?P<thing_id>[^/]+)/properties', viewsets.PropertiesViewSet, basename='property')
