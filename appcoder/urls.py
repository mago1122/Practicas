from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("", inicio),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("profesores/crear", creacion_profesores),
    path("cursos/re-locos", cursos, name="coder-cursos"),
    path("entregables/", entregables, name="coder-entregables"),
    path("curso/crear/", creacion_curso)
]