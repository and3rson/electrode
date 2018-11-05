from django.contrib import admin

from electrode.things import models

admin.site.register(models.Thing, admin.ModelAdmin)
admin.site.register(models.Property, admin.ModelAdmin)
