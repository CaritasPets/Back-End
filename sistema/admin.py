from django.contrib import admin

from .models import Organizacao, Pet, Perdidos

admin.site.register(Organizacao)
admin.site.register(Pet)
admin.site.register(Perdidos)
