from rest_framework import serializers
from rest_framework.reverse import reverse

from electrode.domains import models
from electrode.things.serializers import ThingSerializer


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'url', 'owner', 'display_name', 'actions')
        model = models.Domain

    actions = serializers.SerializerMethodField()

    def get_actions(self, instance):
        return {
            'thing-list': reverse('thing-list', args=(instance.id,), request=self.context.get('request'))
        }


class DomainDetailSerializer(DomainSerializer):
    class Meta(DomainSerializer.Meta):
        fields = DomainSerializer.Meta.fields + ('things',)

    things = ThingSerializer(many=True, read_only=True)
