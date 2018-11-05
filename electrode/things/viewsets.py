from rest_framework import viewsets

from electrode.things import models, serializers


class ThingsViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ThingDetailSerializer
        return serializers.ThingSerializer

    def get_queryset(self):
        return models.Thing.objects.filter(
            domain_id=self.kwargs['domain_id']
        ).prefetch_related('properties')

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['domain'] = self.kwargs['domain_id']
        return super().create(request, *args, **kwargs)


class PropertiesViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PropertyDetailSerializer
        return serializers.PropertySerializer

    def get_queryset(self):
        return models.Property.objects.filter(
            thing__domain_id=self.kwargs['domain_id'],
            thing_id=self.kwargs['thing_id']
        )

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['domain'] = self.kwargs['domain_id']
        request.data['thing'] = self.kwargs['thing_id']
        return super().create(request, *args, **kwargs)
