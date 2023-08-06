from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('', views.ingresoPanel, name='ingresoPanel'),
    path('Productos', views.productos, name='productos'),
    path('Tienda', views.tienda, name='tienda'),
    path('eliminarProducto/<str:idProducto>', views.eliminarProducto, name='eliminarProducto'),        
    path('asignarProducto',views.asignarProducto,name='asignarProducto'),
    path('verProducto/<str:idTienda>', views.verProducto, name ='verProducto'),
    path('eliminarProductoTienda/<str:idProducto>', views.eliminarProductoTienda, name='eliminarProductoTienda'),
    path('eliminarTienda/<str:idTienda>', views.eliminarTienda, name ='eliminarTienda')
    


]
