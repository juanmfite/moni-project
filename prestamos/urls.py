from django.urls import path
from . import views

urlpatterns = [
    path('administrador', views.administrador, name='administrador'),
    path('deletePrestamo/<int:pk>', views.deletePrestamo, name='deletePrestamo'),
    path('prestamo/<int:pk>/edit/', views.prestamo_edit, name='prestamo_edit'),
    path('', views.index, name='index'),
    path('api/prestamos', views.PrestamoList.as_view(), name='PrestamoList'),
]