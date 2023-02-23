from django.contrib import admin
from .models import * 

# Es importante importar todos los modelos para que funcione todo 

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)




# Register your models here.
