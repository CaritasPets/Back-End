from django.contrib import admin

from .models import Organizacao, Porte, Raca, Usuario, Voluntario, Pet, Perdidos

admin.site.register(Organizacao)
admin.site.register(Porte)
admin.site.register(Raca)
admin.site.register(Usuario)
admin.site.register(Voluntario)
admin.site.register(Pet)
admin.site.register(Perdidos)
