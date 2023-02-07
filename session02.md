# Sesión 2: Estructura de un Proyecto en Django

La estructura de un proyecto en Django es una estructura bien definida y organizada que se compone de varios elementos clave. Aquí están los elementos principales de una estructura de proyecto de Django:

1. Directorio del proyecto: Este es el directorio raíz que contiene todos los demás elementos del proyecto, como los directorios de aplicaciones, archivos de configuración y archivos estáticos.

2. Archivo manage.py: Este es un script que se utiliza para gestionar el proyecto de Django, como el inicio de servidor de desarrollo, la creación de la base de datos y la ejecución de comandos.

3. Archivos estáticos: Este es un directorio que contiene archivos estáticos, como imágenes, CSS y JavaScript, que se utilizan en la aplicación. Este directorio hay que crearlo ejecutando:

````
mkdir static
````

4. Archivos de plantilla: Este es un directorio que contiene las plantillas HTML que se utilizan para presentar los datos en la aplicación. Este directorio hay que crealo ejecutando:

````
mkdir templates
````

## El archivo setting.py.

El archivo settings.py en Django es un archivo de configuración que contiene todas las opciones y configuraciones para un proyecto de Django. Este archivo es importante ya que define la forma en que Django funciona y se comporta. Este archivo se encuentra dentro del directoio del proyecto.

Aquí están algunas de las cosas que se pueden configurar en el archivo settings.py:

- Configuración de la base de datos: Se puede especificar el tipo de base de datos que se utilizará, la dirección y el nombre de la base de datos, y las credenciales de acceso.

- Configuración de la zona horaria y el idioma: Se pueden especificar la zona horaria y el idioma que se utilizarán en la aplicación.

- Configuración de la seguridad: Se pueden especificar las opciones de seguridad, como la clave secreta que se utiliza para encriptar los datos y la configuración de la seguridad HTTP.

- Configuración de los archivos estáticos: Se pueden especificar las opciones de los archivos estáticos, como la ruta donde se almacenan los archivos estáticos y cómo se deben servir.

- Configuración de las plantillas: Se pueden especificar las opciones de las plantillas, como la ruta donde se almacenan las plantillas y cómo se deben procesar.

En resumen, el archivo settings.py en Django es un archivo clave que permite a los desarrolladores configurar y personalizar su proyecto de Django. Es importante que este archivo se configure adecuadamente para que la aplicación funcione de manera eficiente y segura.

Más adelaten vamos a revisar mas en detalle el archivo setting del proyecto

## Ejecutar las migraciones

Inicialmente debemos ejucutar nuestras migraciones para crear nuestra base de dato. Por defecto django trabaja con sqlite, pero se pueden configurar desde el settings.py otros motores de base de datos.

Para correr las migraciones abrimos consola y ejecutamos


`````
python manage.py migrate
``````

El comando 'python manage.py migrate' en Django se utiliza para aplicar cualquier cambio en las tablas de la base de datos asociadas con el modelo de la aplicación. Este comando actualiza la estructura de la base de datos para reflejar cualquier cambio realizado en los modelos de la aplicación.


Cuando se crea un nuevo modelo en Django, es necesario ejecutar el comando 'python manage.py makemigrations'
para generar archivos de migración, que describen los cambios que se deben realizar en la estructura de la base de datos.


`````
python manage.py makemigrations
``````

El comando makemigrations es útil porque permite a los desarrolladores generar archivos de migración de manera sencilla, sin tener que escribir manualmente el código SQL necesario para realizar los cambios en la base de datos. También permite mantener un registro de los cambios realizados en la base de datos a lo largo del tiempo.

### Crear un usuario superuser para el proyecto

El usuario administrador se crea mediante una línea de comando y se pide información básica, como nombre de usuario, correo electrónico y contraseña. Después de crear un usuario administrador, se puede acceder a la página de administración de la aplicación usando el nombre de usuario y la contraseña proporcionados.

El comando 'python manage.py createsuperuser' en Django es un comando que se utiliza para crear un usuario administrador en la aplicación. Este usuario tiene acceso completo a la administración de la aplicación y puede realizar tareas administrativas, como agregar, editar y eliminar registros, administrar usuarios y más.

Para crear un usuario administrador ejecuta:

`````
python manage.py createsuperuser
`````

Con el usuario administrador creado ya puedes ingresar a la zona de administración de django. Siguiendo los siguientes pasos:

Corremos nuestro servidor

``````
python manage.py runserver
``````

Accede a la administración del sitio desde un navegador: Abre un navegador y accede a la URL "http://127.0.0.1:8000/admin" se te pedira el usuario y la contraseña del superuser que creaste en el paso anterior.

¡Buen trabajo, Henrry!

