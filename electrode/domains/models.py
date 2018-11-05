from django.db import models

from electrode.main.models import SlugPrimaryKeyMixin, OwnerMixin


class Domain(SlugPrimaryKeyMixin, OwnerMixin, models.Model):
    display_name = models.TextField(null=False, blank=False)

    def __repr__(self):
        return f'Domain id={self.id} "{self.display_name}"'

    __str__ = __repr__
