
# Control de Prestamos para Test de Moni

Este es un proyecto hecho en Django en el que se resuelve la consigna del test técnico.

### Especificaciones 📋

- Django 2.2
- Postgres 11.2
- Bootstrap
- Django Rest Framework
- Docker (docker-compose)

### Pre-requisitos

Se debe tener instalado docker y docker-compose. 

Tener libre el puerto 8000. 

### Despliegue 🔧

Se utilizó un contenedor Docker para dicho proyecto. El mismo esta hecho con un _docker-compose_.

Para desplegar el proyecto simplemente se debe ejecutar el script _init.sh_, el mismo contiene todos los comandos de docker junto con importanción de la base de datos.


_Explicación del funcionamiento del docker-compose_

En el docker-compose se crearon dos servicios, uno para la web y otro la base de datos. 

Para el servicio de la base de datos no se creo un volumen ya que se hizo un dump con algunos datos y luegos son cargados en la inicialización. Y para el servicio de la web se realiza el comando _runserver_ de Django para iniciar el servidor de desarrollo del mismo. 

_Explicación del funcionamiento del script iniciador_

Dicho script levanta la base de datos y hace un sleep porque suele demorar unos pocos segundos en quedar lista la base de datos, sino puede haber conflictos si se crea la web antes que la base.

Luego se copia el archivo _corbis-stock.dump_ que tiene todos los datos de prueba y se importan a la base de datos ya creada.

Finalmente se levanta el servicio de la web y ya está listo para utilizar en _localhost:8000_.

## Usuario
Usuario de administración:

    user: moniadmin , pass: moni1234


## Modelo de la Base de Datos
Es un modelo muy simple que se realizó con dos tablas, una para los Prestamo y otra tabla para los tipos de Genero. Esto se hizo así ya que cuando se trata de tipos en general, es bueno hacer una tabla aparte donde estén contenidos todos los tipos. Ya que si esta tabla no estuviera entonces podría darse el caso de que, por ejemplo, se creer un genero "Masculino", otro "masculino", otro "M" u otro "m". Entonces si se quieren filtrar sería engorroso darse de cuenta de todas las formas en las que fueron escritas. 

## Otros
Se creó un método que devuelve todos los prestamos utilizando Django Rest Framework.

Dicho método se puede ver en _localhost:8000/api/prestamos_