from django.urls import path
from APP_Libreria.views import *
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", clientes, name="clientes"),
    path("resenia/", resenias, name="resenia"),
    path("listarResenia/",ReseniaList , name="listarResenia"),
    path("empleados/", empleados, name="empleados"),
    path("empleados/empleados/list", Empleadoslist.as_view(), name="empleados_list"),
    path(r"^(?P<pk>\d+)$", Empleadodetalle.as_view(), name="DetalleEmpleado"),
    path(r"^editar/(?P<pk>\d+)$", Empleadouppdate.as_view(), name="EditarEmpleado"),
    path(r"^borrar/(?P<pk>\d+)$", Empleadoelimina.as_view(), name="BorrarEmpleado"),
    path("empleados/empleado_nuevo/", EmpleadoNuevo, name="empleado_nuevo"),
    path("stock/", stock, name="stock"),
    path("busquedaStock/", busquedaStock, name="busquedaStock"),
    path("buscar/", buscar, name="buscar"),
    path("buscarlibro/", buscarlibro, name="buscarlibro"),
    path("buscargenero/", buscargenero, name="buscargenero"),
    path("stock/list", listStock.as_view(), name="ListaStock"),
    path(r'^(?P<pk>\d+)$', detalleStock.as_view(), name="DetailleStock"),
    #path(r'^nuevo)$', nuevoStock.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', uppdateStock.as_view(), name="EditarStock"),
    path(r'^borrar/(?P<pk>\d+)$', eliminaStock.as_view(), name="BorrarStock"),
    #path("login/", login_request, name="Login"),
    #path("registroUsuario/", registracion, name="RegistroUsuario"),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")
    ]