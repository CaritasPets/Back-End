from django.contrib import admin

from .models import Organizacao, Raca, Pet, Perdidos, Membro

admin.site.register(Organizacao)
admin.site.register(Raca)
admin.site.register(Pet)
admin.site.register(Perdidos)
admin.site.register(Membro)
