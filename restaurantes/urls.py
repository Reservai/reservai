from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name="cadastro"),
    path('login', views.login, name="login"),
]