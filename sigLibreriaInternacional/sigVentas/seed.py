from django.db import models
from django_seed import Seeder
from .models import Usuario

class datosFake(Seeder):

    def run(self, *args, **kwargs):
        # Cargar los datos del archivo JSON
        with open('initial_data.json') as data_file:
            data = json.load(data_file)

        # Insertar datos en la tabla Usuario
        for item in data:
            self.seed(data=item)
