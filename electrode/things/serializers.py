from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_nested.relations import NestedHyperlinkedIdentityField

from electrode.things import models


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'url', 'domain', 'display_name', 'actions')
        model = models.Thing

    actions = serializers.SerializerMethodField()
    url = NestedHyperlinkedIdentityField(view_name='thing-detail', parent_lookup_kwargs={'domain_id': 'domain_id'})

    def get_actions(self, instance):
        return {
            'property-list': reverse('property-list', args=(instance.domain_id, instance.id), request=self.context.get('request'))
        }


class ThingDetailSerializer(ThingSerializer):
    class Meta(ThingSerializer.Meta):
        fields = ThingSerializer.Meta.fields + ('properties',)

    properties = serializers.SerializerMethodField()

    def get_properties(self, instance):
        return PropertySerializer(instance.properties.all(), many=True, context=self.context).data


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'url', 'thing', 'display_name', 'type', 'value')
        model = models.Property

    url = NestedHyperlinkedIdentityField(view_name='property-detail', parent_lookup_kwargs={'domain_id': 'thing__domain_id', 'thing_id': 'thing_id'})


class PropertyDetailSerializer(PropertySerializer):
    pass
