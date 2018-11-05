from django.contrib import admin

from electrode.domains import models

admin.site.register(models.Domain, admin.ModelAdmin)
