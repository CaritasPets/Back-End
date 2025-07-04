from django.contrib import admin

from .models import Organizacao, Porte, Raca, Usuario, Voluntario

admin.site.register(Organizacao)
admin.site.register(Porte)
admin.site.register(Raca)
admin.site.register(Usuario)
admin.site.register(Voluntario)
