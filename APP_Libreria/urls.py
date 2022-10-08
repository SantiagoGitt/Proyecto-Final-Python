from django.urls import path
from APP_Libreria.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", clientes, name="clientes"),
    path("resenia_nueva/", resenias, name="reseña_nueva"),
    path("resenia", ReseniaList.as_view(), name="resenia"),
    #path("empleados/", empleados, name="empleados"),
    path("empleados", Empleadoslist.as_view(), name="empleados"),
    path("empleados/<pk>", Empleadodetalle.as_view(), name="empleados_detalle"),
    path("empleados/editar/<pk>", Empleadouppdate.as_view(), name="empleados_edit"),
    path("empleados/borrar/<pk>", Empleadoelimina.as_view(), name="empleados_borrar"),
    path("empleado_nuevo/", EmpleadoNuevo, name="empleado_nuevo"),
    path("stock/", stock, name="stock"),
    path("busquedaStock/", busquedaStock, name="busquedaStock"),
    path("buscarautor/", buscarautor, name="buscarautor"),
    path("buscarlibro/", buscarlibro, name="buscarlibro"),
    path("buscargenero/", buscargenero, name="buscargenero"),
    path("stocks/lista/", Stocklist.as_view(), name="stock_lista"),
    path("stocks/<pk>", Stockdetalle.as_view(), name="stock_detalle"),
    path("stocks/nuevo/", Stocknuevo.as_view(), name="stock_nuevo"),
    path("stocks/editar/<pk>", Stockuppdate.as_view(), name="stock_edit"),
    path("stocks/borrar/<pk>", Stockelimina.as_view(), name="stock_borrar"),
    path("about/", about, name="about")
    #path("login/", login_request, name="Login"),
    #path("registroUsuario/", registracion, name="RegistroUsuario"),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")
    ]