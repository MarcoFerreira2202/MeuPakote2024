"""meu_pacote_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from accounts import views
from app_meu_pacote import views as app_meu_pacote_views
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_meu_pacote_views.index, name='index'),
    path('encomendas_pendentes/', app_meu_pacote_views.encomendas_pendentes, name='encomendas_pendentes'),
    path('minhas_encomendas/', app_meu_pacote_views.minhas_encomendas, name='minhas_encomendas'),
    path('encomendas_entregues/', app_meu_pacote_views.encomendas_entregues, name='encomendas_entregues'),
    path('cadastrar_encomenda/', app_meu_pacote_views.cadastrar_encomenda, name='cadastrar_encomenda'),
    path('encomenda/<int:encomenda_id>', app_meu_pacote_views.encomenda, name='encomenda'),
    path('logout/', app_meu_pacote_views.logout_view, name='logout'),
    path('cadastrar_morador/', app_meu_pacote_views.cadastrar_morador, name='cadastrar_morador'),
    path('cadastrar_funcionario/', app_meu_pacote_views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('login/', accounts_views.login_view, name='login_view'),
    path('signup/', accounts_views.signup_view, name='signup_view'),
]
