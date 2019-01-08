% prepara el repositorio para su despliegue. 
release: sh -c 'cd musicapp && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd musicapp && gunicorn musicapp.wsgi --log-file -'