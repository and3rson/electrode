from django.conf.urls import url
from rest_framework_nested.routers import SimpleRouter

from electrode.domains import viewsets

router = SimpleRouter(trailing_slash=False)
router.register('domains', viewsets.DomainsViewSet, basename='domain')
