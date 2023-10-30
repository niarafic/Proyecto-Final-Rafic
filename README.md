# laboldm

El proyecto consiste en la página de un laboratorio de una universidad. La aplicación inicio contiene tres modelos:

1- Integrantes: Sirve para representar a cada uno de los miembros del laboratorio. Cada integrante está identificado por su nombre, apellido, dirección de e-mail y por su área de trabajo. Se pueden crear nuevos integrantes mediante un botón en el margen superior izquierdo que nos lleva a un formulario. En http://127.0.0.1:8000/integrantes/ se puede visualizar la lista de integrantes.

2- Publicaciones: Sirve para representar las publicaciones científicas del laboratorio. Cada publicación está identificada por la información necesaria para poder citarla en las referencias de un artículo científico: el título, los autores, la revista donde fue publicado, el volumen de la revista y el año de publicación. Se pueden agregar nuevas publicaciones mediante un botón en el margen superior izquierdo que nos lleva a un formulario. En http://127.0.0.1:8000/publicaciones/ se puede visualizar la lista de publicaciones. Como en general la lista de publicaciones de un laboratorio suele ser muy extensa, además se agregó un botón de búsqueda mediante el nombre de la publicación.

3- Colaboradores: Sirve para representar a los colaboradores externos del laboratorio (es decir, investigadores de otras universidades con los que se tienen proyectos de investigación en común). Cada colaborador está identificado por su nombre, apellido, e-mail y universidad donde trabaja.  Se pueden agregar nuevos colaboradores mediante un botón en el margen superior izquierdo que nos lleva a un formulario. En http://127.0.0.1:8000/colaboradores/  se puede visualizar la lista de colaboradores.

