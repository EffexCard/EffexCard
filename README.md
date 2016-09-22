SISTEMA EFFEXCARD VERSION 1.3
 - http://DOMINIO/website
 - http://DOMINIO/store
 - http://DOMINIO/login

INSTALACIÓN:

PASO 1: Clonar en su equipo el repositorio del proyecto, con sus cuentas respectivas. 

   git clone git@github.com:EffexCard/EffexCard.git

PASO 2: Crear el entorno virtual con virtualenv, para el instalar virtualenv pueden seguir el siguiente tutorial (https://virtualenv.pypa.io/en/stable/installation/). 
   mkvirtualenv effexcard

PASO 3: Dentro de la carpeta del proyecto, Instalar las dependencias desde el archivo requirements.txt
   pip install -R requirements.txt

PASO 4: Crear las bases de datos
   createdb effexcard

PASO 5: Verificar los datos de acceso a la base de datos en el archivo /effexcard/settings.py

PASO 6: Dentro de la carpeta del proyecto, sincronizar la base de datos con el siguiente comando
   python manage.py migrate

PASO 7: Levantar el servidor del proyecto
   python manage.py runserver 80

Para instalar el proyecto en Heroku, seguir los siguientes tutoriales. 
   - https://devcenter.heroku.com/articles/getting-started-with-python	
   - https://devcenter.heroku.com/articles/deploying-python

<a href="http://lightpath.io">LightPath Team 2016</a> 