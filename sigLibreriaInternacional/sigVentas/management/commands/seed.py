from django.core.management.base import BaseCommand
from sigVentas.models import Usuario, Proveedor, Pedido, Producto

class Command(BaseCommand):
    help = 'Carga datos desde un archivo JSON a la base de datos'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        with open(filename) as json_file:
            data = json.load(json_file)

            for obj in data:
                model_name = obj.get('model')
                fields = obj.get('fields')

                if model_name == 'sigVentas.Usuario':
                    Usuario.objects.create(**fields)
                elif model_name == 'sigVentas.Proveedor':
                    Proveedor.objects.create(**fields)
                elif model_name == 'sigVentas.Pedido':
                    Pedido.objects.create(**fields)
                elif model_name == 'sigVentas.Producto':
                    Producto.objects.create(**fields)

        self.stdout.write(self.style.SUCCESS('¡Datos cargados exitosamente!'))