from django.db import models
from django.contrib.postgres.fields import JSONField

from electrode.main.models import SlugPrimaryKeyMixin, OwnerMixin


class Thing(SlugPrimaryKeyMixin, models.Model):
    domain = models.ForeignKey('domains.Domain', null=False, blank=False, on_delete=models.CASCADE, related_name='things')
    display_name = models.TextField(null=False, blank=False)

    def __repr__(self):
        return f'Thing id={self.id} "{self.display_name}"'

    __str__ = __repr__


class Property(SlugPrimaryKeyMixin, models.Model):
    class Meta:
        verbose_name_plural = 'Properties'

    TYPES = (
        ('temperature', 'Temperature (deg C)'),
        ('humidity', 'Humidity (%)'),
        ('speed', 'Speed (km/h)'),
        ('power', 'Power (W)'),
        ('distance', 'Distance (m)'),
        ('rotation', 'Rotation (deg)'),
        ('brightness', 'Brightness (%)'),
        ('image', 'Image (URL)'),
        ('state', 'State (on/off)'),
        ('direction', 'Direction'),
        ('other', 'Other'),
    )

    thing = models.ForeignKey('Thing', null=False, blank=False, on_delete=models.CASCADE, related_name='properties')
    display_name = models.TextField(null=False, blank=False)
    type = models.CharField(max_length=16, null=False, blank=False, choices=TYPES)
    value = JSONField(null=True, blank=True, default=None)

    @property
    def display_type(self):
        return dict(self.TYPES)[self.type]

    def __repr__(self):
        return f'Property id={self.id} type={self.type} "{self.display_name}"'

    __str__ = __repr__
