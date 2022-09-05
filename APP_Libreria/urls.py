from django.urls import path
from APP_Libreria.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", clientes, name="clientes"),
    path("empleados/", empleados, name="empleados"),
    path("stock/", stock, name="stock"),
    path("resenia/", resenia, name="resenia"),
    path("clienteFormulario/", clienteFormulario, name="clienteFormulario"),

]