from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurante/cadastro', views.cadastro, name="cadastro"),
    path('restaurante/login', views.login, name="login"),
]