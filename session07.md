## URL canónicas para modelos

Las URL canónicas son una representación única y permanente de un recurso en la web. En Django, las URL canónicas se utilizan para asegurarse de que cada objeto en un modelo tenga una URL única y permanente que se pueda usar para acceder a sus detalles en el navegador.

En Django, las URL canónicas se definen en el modelo usando el atributo get_absolute_url. Este atributo es un método que devuelve la URL canónica para un objeto en particular. Aquí está un ejemplo:

`````
from django.urls import reverse

class Post(models.Model):
    # ... other fields ...
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.publish.year),
                                                  str(self.publish.month),
                                                  str(self.publish.day),
                                                  self.slug])
`````

En este ejemplo, el método get_absolute_url devuelve la URL canónica para un objeto Post utilizando la función reverse de Django. La función reverse toma un nombre de URL y argumentos y devuelve la URL correspondiente. En este caso, se está utilizando el nombre de URL 'blog:post_detail' y los argumentos correspondientes al año, mes, día y slug de la publicación para generar la URL canónica.

Una vez que se ha definido el atributo get_absolute_url en el modelo, se puede acceder a la URL canónica de un objeto en cualquier parte de la aplicación simplemente llamando a obj.get_absolute_url(). Por ejemplo:

``````
post = Post.objects.get(pk=1)
url = post.get_absolute_url()
``````

Es importante destacar que las URL canónicas son opcionales en Django, pero son muy útiles para mantener una representación permanente de los objetos en una aplicación y para facilitar la creación de enlaces a ellos en el código.


## Los templates en django

Los templates en Django son archivos que contienen una marcación HTML y etiquetas especiales que se utilizan para renderizar contenido dinámico en una página web. En Django, los templates se utilizan para definir la estructura y el diseño de las páginas web de una aplicación.

Los templates en Django se pueden personalizar fácilmente para incluir contenido dinámico generado por las vistas en la aplicación. Por ejemplo, supongamos que tiene una vista que muestra una lista de publicaciones en su aplicación. La vista puede enviar la lista de publicaciones a un template, que luego puede iterar sobre la lista y mostrar cada publicación en la página web.

Los templates en Django se almacenan en una carpeta especial en la aplicación llamada templates y se pueden reutilizar y personalizar fácilmente en diferentes vistas y aplicaciones. Esto permite crear aplicaciones con un diseño consistente y una estructura de página común.

Creamos nuestro directorio llamado templates en la carpeta principal de nuestro proyecto.





