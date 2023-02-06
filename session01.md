## Sesión 1: Configuración del Enterno de Desarrollo

1 . Crear un entorno virtual

Crear un entorno virtual: Para crear un entorno virtual, puedes ejecutar el siguiente comando en tu terminal, reemplazando "nombre_del_entorno" con el nombre que quieras darle a tu entorno virtual:

````
virtualenv nombre_del_entorno
````

Por adopción de la comunidad el enterno virtual se debe llamar venv
aunque se puede eligir otro nombre.

2. Activar el entorno virtual: Para activar el entorno virtual, ejecuta el siguiente comando en tu terminal, reemplazando "nombre_del_entorno" con el nombre que le diste a tu entorno virtual:


`````
source nombre_del_entorno/bin/activate
`````

3. Se debe crear un la raiz del proyecto un archivo requirements.txt

`````
nano requirements.txt
`````

El archivo requirements.txt en Python es un archivo de texto que contiene una lista de los paquetes de Python necesarios para ejecutar un proyecto específico. Cada línea en este archivo contiene el nombre de un paquete y, a veces, una versión específica requerida.

Este archivo es útil para varios propósitos:

- Documentación: El archivo requirements.txt documenta las dependencias del proyecto, lo que puede ser útil para otros desarrolladores que deseen trabajar en el proyecto.

- Reproducibilidad: Al tener un registro de los paquetes necesarios para ejecutar un proyecto, es más fácil replicar el entorno de desarrollo en otras máquinas o sistemas.

- Automatización: El archivo requirements.txt puede ser utilizado por herramientas de automatización como pip para instalar automáticamente todas las dependencias requeridas para ejecutar el proyecto.

- En resumen, el archivo requirements.txt es una parte importante de la gestión de dependencias en Python y es una práctica común incluirlo en los proyectos de Python para garantizar la documentación, la reproducibilidad y la automatización de las dependencias.

A nuestro archivo requirements.txt vamos a agregar la siguiente linea:

`````
Django>=3.2,<3.3
`````

La línea Django>=3.2,<3.3 especifica que se requiere la versión 3.2 o superior de Django, pero menor que la versión 3.3.

4. Para instalar las dependencias de nuestro proyecto ejecutamos desde el terminal

`````
pip install -r requirements.txt
``````

El comando pip install -r requirements.txt se utiliza para instalar los paquetes de Python que están especificados en un archivo requirements.txt. Este archivo contiene solo contiene la versión de django que vamos a utilizar. 

Una vez instalado todos las de nuestro proyecto podemos revisar las dependencias de Python instaladas en un entorno virtual ejecutando

`````
pip freeze
`````

5. Para crear un nuevo proyecto de django ejecutamos:

``````
python3 venv/bin/django-admin.py startproject henrryweb .
``````

El comando python3 venv/bin/django-admin.py startproject henrryweb . es un comando para crear un nuevo proyecto de Django.

El comando tiene los siguientes componentes:

1. python3: Este es el intérprete de Python que se utilizará para ejecutar el siguiente comando.

2. venv/bin/django-admin.py: Este es el script django-admin.py que viene con la instalación de Django. Este script se utiliza para crear nuevos proyectos, gestionar la base de datos, entre otras tareas relacionadas con Django. venv/bin es la ubicación donde se encuentra el script en el entorno virtual creado.

3. startproject: Este es un argumento para el script django-admin.py que indica que se desea crear un nuevo proyecto de Django.

4. henrryweb: Este es el nombre del proyecto de Django que se desea crear.

5. '.': Este es el directorio de destino en el que se creará el nuevo proyecto de Django. El punto . indica que se creará en el directorio actual.

En resumen, este comando se utiliza para crear un nuevo proyecto de Django utilizando el intérprete de Python3 y el script django-admin.py en un entorno virtual. El nuevo proyecto se creará en el directorio actual y se llamará henrryweb.

6. Verifica que tu proyecto está funcionando: Puedes verificar que tu proyecto está funcionando ejecutando el siguiente comando:

`````
python manage.py runserver
`````

Accede a tu proyecto en un navegador: Abre un navegador y accede a la URL "http://127.0.0.1:8000/" para verificar que tu proyecto está funcionando correctamente.

Con estos pasos deberías tener un proyecto de Django recién creado y funcionando.

¡Buen trabajo, Henrry!

