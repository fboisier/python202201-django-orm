from django.urls import path
from . import views

# http://127.0.0.1:8000/usuarios/

app_name = 'usuarios'

urlpatterns = [
    path('', views.list_usuarios, name='listado' ),
    path('add/', views.add_usuarios, name='agregar' ),
    path('edit/<int:id>', views.edit_usuarios, name='editar' ),
    path('delete/<int:id>', views.delete_usuarios, name='eliminar' ),
    path('delete/<int:id>/ajax', views.delete_usuarios_api, name='eliminar_ajax' ),
]
