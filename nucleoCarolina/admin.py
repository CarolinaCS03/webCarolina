from django.contrib import admin

# Register your models here.
from nucleoCarolina.models import AnimalMascota
from nucleoCarolina.models import Raza
from nucleoCarolina.models import Mascota
from nucleoCarolina.models import Cita
from nucleoCarolina.models import HistorialCita
from nucleoCarolina.models import Vacuna
from nucleoCarolina.models import Vacunacion

# Register your models here.
admin.site.register(AnimalMascota)
admin.site.register(Raza)
admin.site.register(Mascota)
admin.site.register(Cita)
admin.site.register(HistorialCita)
admin.site.register(Vacuna)
admin.site.register(Vacunacion)