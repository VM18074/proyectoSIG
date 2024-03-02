#Tutorial de comandos basicos

#CREAR MIGRACIONES:
> py manage.py makemigrations sigVentas  

#CORRER MIGRACIONES:
> py manage.py sqlmigrate sigVentas 0002 ->Este numero final ira cambiando a medida se creen nuevas migraciones


#CORRER SEEDS:
> python manage.py loaddata sigVentas/initial_data.json  

#INICIAR SERVIDOR:
> py manage.py runserver 
