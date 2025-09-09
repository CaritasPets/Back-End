from django.contrib import admin
from users.models import User, Organization

admin.site.register(Organization)
admin.site.register(User)