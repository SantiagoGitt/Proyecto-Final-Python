from django.urls import path
from APP_Libreria.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", clientes, name="clientes"),
    path("resenia", ReseniaList.as_view(), name="resenia"),
    path("resenia/editar/<pk>", Reseniauppdate.as_view(), name="resenia_edit"),
    path("resenia/borrar/<pk>", Reseniaelimina.as_view(), name="resenia_borrar"),
    path("resenia/nuevo/", Resenianueva.as_view(), name="resenia_nueva"),
    #path("empleados/", empleados, name="empleados"),
    path("empleados", Empleadoslist.as_view(), name="empleados"),
    path("empleados/<pk>", Empleadodetalle.as_view(), name="empleados_detalle"),
    path("empleados/editar/<pk>", Empleadouppdate.as_view(), name="empleados_edit"),
    path("empleados/borrar/<pk>", Empleadoelimina.as_view(), name="empleados_borrar"),
    path("empleados/nuevo/", Empleadonuevo.as_view(), name="empleado_nuevo"),
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
    path("about/", about, name="about"),
    path("login/", login_request, name="login"),
    path("registrousuario/", registracion, name="registrousuario"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarperfil/", EditarPerfil, name="editarperfil"),
    path("agregaravatar/", cargaravatar, name="agregaravatar")
    ]