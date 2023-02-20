## Los templates en django

Los templates en Django son archivos que contienen una marcación HTML y etiquetas especiales que se utilizan para renderizar contenido dinámico en una página web. En Django, los templates se utilizan para definir la estructura y el diseño de las páginas web de una aplicación.

Los templates en Django se pueden personalizar fácilmente para incluir contenido dinámico generado por las vistas en la aplicación. Por ejemplo, supongamos que tiene una vista que muestra una lista de publicaciones en su aplicación. La vista puede enviar la lista de publicaciones a un template, que luego puede iterar sobre la lista y mostrar cada publicación en la página web.

Los templates en Django se almacenan en una carpeta especial en la aplicación llamada templates y se pueden reutilizar y personalizar fácilmente en diferentes vistas y aplicaciones. Esto permite crear aplicaciones con un diseño consistente y una estructura de página común.

Creamos nuestro directorio llamado templates en la carpeta principal de nuestro proyecto.

````
mkdir templates
`````

Debemos expecificar en nuestro settings.py la carpeta de los templates

`````
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates"], // aqui.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
`````

Esta línea de código es parte de la configuración de los templates en Django. Se está especificando la ubicación de los archivos de plantilla en el sistema de archivos.

La constante BASE_DIR se refiere a la raíz de la aplicación de Django, es decir, la ubicación del archivo settings.py. La ubicación de los archivos de plantilla se define como BASE_DIR / "templates", lo que significa que los archivos de plantilla se encuentran en una carpeta llamada "templates" dentro de la raíz de la aplicación de Django.

Considerar tambien dentro del directorio templates crear un subdirectorio
snippets con el objetivo de dividir los elementos comunes de nuestra plantillas como lo es el header y el footer y reutiizarlo cada vez que lo necesitemos en nuestros templates

`````
cd templates
mkdir snippets
`````

## Template base.html

El template base en Django es una plantilla que es utilizada como base para otras plantillas en la aplicación. Normalmente, incluye elementos comunes a todas las páginas, como el encabezado, el pie de página y el menú de navegación.

Aquí hay algunos elementos que pueden ser incluidos en un template base en Django:

- Encabezado: Este puede incluir el título de la página, el logotipo, el menú de navegación y cualquier otro elemento que desees incluir en la parte superior de cada página.

- Bloques de contenido: Estos son bloques de contenido que serán reemplazados por el contenido de las plantillas hijas. Por ejemplo, un bloque de contenido puede ser el contenido principal de la página.

- Pie de página: Este puede incluir información sobre la empresa, enlaces a las políticas de privacidad y términos de uso, y cualquier otro elemento que desees incluir en la parte inferior de cada página.

- JavaScript y estilos CSS: Estos se pueden incluir en el template base para asegurarte de que se carguen en todas las páginas de la aplicación.

El template base en Django también puede incluir directivas de template, como {% block %} y {% extends %}, que permiten a las plantillas hijas heredar el contenido del template base y reemplazar o agregar contenido en los bloques de contenido.

En los templates en django vamos a encontrar siempre tag y filter, variables dentro de nuestro html para que nuestro contenido sea dinamico.


## Template Tags

Los template tags son fragmentos de código personalizados que se utilizan en los templates de Django para realizar tareas específicas. Estos tags se definen en módulos de Python y se incluyen en las plantillas mediante la directiva {% tag_name %}.

Algunos ejemplos de template tags en Django incluyen:

1. {% for %}: Este template tag se utiliza para iterar sobre una secuencia, como una lista o un diccionario, y realizar una acción en cada elemento de la secuencia.

2. {% if %}: Este template tag se utiliza para evaluar una expresión y realizar una acción si la expresión es verdadera.

3. {% url %}: Este template tag se utiliza para resolver una URL a partir de un nombre de URL en la aplicación.

4. {% static %}: Este template tag se utiliza para construir una URL para un archivo estático en la aplicación.

Los template tags permiten a los desarrolladores de Django realizar tareas complejas en los templates sin tener que escribir código Python en el template. Esto ayuda a mantener la separación de preocupaciones y a mejorar la legibilidad y la organización del código.

Además, Django tiene un conjunto integrado de template tags para realizar tareas comunes, como la gestión de formularios, la gestión de mensajes y la traducción de texto. Sin embargo, también podemos crear nuestros propios template tags personalizados para satisfacer sus necesidades específicas.

## Template filter

Los filtros de plantilla son funciones personalizadas que se utilizan en los templates de Django para transformar datos y realizar tareas específicas. Estos filtros se definen en módulos de Python y se aplican a los datos en las plantillas mediante la sintaxis {{ variable|filter }}.

Algunos ejemplos de filtros de plantilla en Django incluyen:

- lower: Este filtro convierte una cadena en minúsculas.

- date: Este filtro formatea un objeto fecha en una cadena de fecha específica.

- truncatewords: Este filtro es útil para mostrar una descripción o resumen de un texto más largo en una página web. 

- linebreaks: Este filtro convierte saltos de línea en etiquetas HTML <br>.

Los filtros de plantilla permiten a los desarrolladores de Django realizar tareas simples de formateo de datos en los templates sin tener que escribir código Python en el template. Esto ayuda a mantener la separación de preocupaciones y a mejorar la legibilidad y la organización del código.

Además, Django tiene un conjunto integrado de filtros de plantilla para realizar tareas comunes, como la formateo de fechas y números. Sin embargo, también pueden se pueden crear sus nuestros propios filtros de plantilla personalizados para satisfacer sus necesidades específicas.


## Templates Variables

Las variables de plantilla son valores que se pasan desde la (vista) a la plantilla en Django. Estas variables se utilizan para mostrar información dinámica en la plantilla.

Por ejemplo, en nuestra aplicación de blog, una vista puede recopilar una lista de publicaciones y pasarlas a una plantilla para mostrar una lista de publicaciones en una página. La plantilla accede a las publicaciones mediante una variable, por ejemplo posts, y las muestra en la página mediante un bucle {% for %} que itera sobre la lista de publicaciones.

Las variables de plantilla se definen en la vista y se pasan a la plantilla como argumento en la función render(). Por ejemplo:

`````
def post_list(request):
    posts = Post.published.all()
    return render(request, 'home.html', {'posts': posts})
`````

En este ejemplo, la vista post_list recopila una lista de todas las publicaciones publicadas y las pasa a la plantilla home.html como una variable llamada posts. La plantilla puede acceder a esta variable y mostrar la información dinámica en la página.

## Directiva {% load static %} en la plantillas

La directiva {% load static %} en una plantilla de Django carga el gestor de archivos estáticos que se utiliza para acceder a los archivos estáticos en la aplicación. Esta directiva se coloca al principio de la plantilla y se usa para cargar el gestor de archivos estáticos antes de utilizar la directiva {% static %} para acceder a los archivos estáticos.

Este archivo se encuentra siempre en la primera linea de nuestro template

Por ejemplo, si queremos incluir un archivo CSS en la plantilla, utilizaríamos la siguiente línea de código:

`````
{% load static %}
	<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'css/swiper.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'css/dark.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'css/font-icons.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'css/animate.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'css/magnific-popup.css' %}" type="text/css" />
`````

En este ejemplo, la directiva {% load static %} carga el gestor de archivos estáticos, y luego se utiliza la directiva {% static %} para construir una URL para el archivo CSS en la aplicación.


## La directiva {% extends %} en la plantillas.

La directiva {% extends %} en una plantilla de Django se utiliza para heredar de una plantilla base. Esta directiva permite a los desarrolladores crear plantillas base que contengan contenido estático y estructura de página común, y luego heredar de esta plantilla base para crear plantillas hijas que agreguen contenido dinámico específico.


Por ejemplo, podemos tener una plantilla base base.html que contenga el encabezado, el pie de página y la estructura básica de la página, y luego crear plantillas hijas que hereden de base.html y agreguen el contenido específico de cada página.

`````
{% extends 'base.html' %}
`````

La directiva {% extends 'base.html' %} indica que la plantilla actual hereda de la plantilla base.html. La plantilla hija puede sobreescribir los bloques de la plantilla base y agregar contenido adicional donde sea necesario.

Este enfoque de herencia de plantillas es una práctica común en Django y nos permite crear y mantener fácilmente un diseño consistente y estructura de página en toda la aplicación.






