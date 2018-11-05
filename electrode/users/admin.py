from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from electrode.users import models

admin.site.register(models.User, UserAdmin)
