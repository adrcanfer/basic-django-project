# Proyecto básico con Django
Este repositorio contiene un projecto de prueba realizado con el framework Django

## ¿Qué necesitamos?
Para lanzar este proyecto sólo necesitaríamos tener Python instalado. 

## ¿Cómo lanzar el proyecto en local? 
Una vez tenemos el proyecto descargado en local, debemos ejecutar las siguientes instrucciones en la linea de comando desde el directorio en el que se encuentra el archivo manage.py:
  - python install -r requirements.txt
  - python manage.py migrate
  - python manage.py createsuperuser (Sólo si queremos acceder a la ventana de administación
  - python manage.py runserver
Tras esto tendremos desplegado el proyecto en local

## ¿Cómo comprobar que se ha lanzado correctamente? 
Abrimos el navegador y accedemos a localhost:8000. Debería salirnos algo así:
![Inicio](https://user-images.githubusercontent.com/19341846/49700766-565ec700-fbe3-11e8-93af-0834622ef0d5.png)

## ¿Qué podemos hacer en la aplicación?
Navegando por las opciones del menú podemos acceder a 3 listados, el primero es el listado de todas las canciones almacenadas en la base de datos, el segundo es el listado de canciones agrupadas por artistas y el tercero agrupadas por géneros. NOTA: Los listados no muestran nada puesto que la base de datos está vacía
![Listado](https://user-images.githubusercontent.com/19341846/49700771-6b3b5a80-fbe3-11e8-938e-3241f4a2071e.png)
Desde el primer listado podemos añadir canciones a la base de datos, desde el segundo podemos crear artistas y desde el tercero géneros musicales. NOTA: Para crear una canción debe existir el autor y el/los género/s de la misma.
![Formulario](https://user-images.githubusercontent.com/19341846/49700748-15ff4900-fbe3-11e8-9ffc-431287262fed.png)
