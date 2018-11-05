from rest_framework import viewsets

from electrode.domains import models, serializers


class DomainsViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DomainDetailSerializer
        return serializers.DomainSerializer

    def get_queryset(self):
        return models.Domain.objects.all().prefetch_related(
            'things', 'things__properties'
        )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
