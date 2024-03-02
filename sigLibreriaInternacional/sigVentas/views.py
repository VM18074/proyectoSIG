from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import RedirectView

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def angular_login_redirect(request):
    return RedirectView.as_view(url='http://localhost:8000/login')(request)

