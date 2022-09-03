from django.urls import path
from APP_Libreria.views import *

urlpatterns = [
    path("", inicio),
    path("clientes/", clientes),
    path("empleados/", empleados),
    path("stock/", stock),
    path("resenia/", resenia),

]