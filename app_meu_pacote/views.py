from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from .models import Encomenda, Morador, Funcionario, Condominio
from .forms import EncomendaForm, UserRegistrationForm, MoradorForm, FuncionarioForm, BaixaEncomendaForm
import datetime

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    return render(request, 'index.html')

def cadastrar_encomenda(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    if request.method == 'POST':
        form = EncomendaForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            msg_sucesso = f'Encomenda "{form.instance.descricao}" para "{form.instance.morador}" cadastrada com sucesso!'
            form = EncomendaForm()
            return render(request, 'cadastrar_encomenda.html', {'msg': msg_sucesso, 'form': form})
    else:
        form = EncomendaForm()
    return render(request, 'cadastrar_encomenda.html', {'form': form})

def encomendas_pendentes(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    encomendas = Encomenda.objects.filter(data_hora_entrega=None)
    context = {'encomendas': encomendas}
    return render(request, 'encomendas_pendentes.html', context)

def encomenda(request, encomenda_id):
    
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    
    encomenda = get_object_or_404(Encomenda, id=encomenda_id)

    if request.method == 'POST':
        form = BaixaEncomendaForm(request.POST)
        if form.is_valid():
            codigo_enviado = str(form.data['codigo_enviado'])
            if codigo_enviado == encomenda.codigo_retirada:
                encomenda.data_hora_entrega = datetime.datetime.now(tz=timezone.utc)
                encomenda.funcionario_entrega = Funcionario.objects.get(user=request.user)
                encomenda.save()
                msg = f'Encomenda "{encomenda.descricao}" para "{encomenda.morador}" baixada com sucesso!'
                return render(request, 'encomenda.html',{'encomenda':encomenda,'msg': msg})
            else:
                msg_error = 'Código informado é inválido!'
                return render(request, 'encomenda.html', {'encomenda':encomenda,'msg_error': msg_error})
    else:
        encomenda = get_object_or_404(Encomenda, id=encomenda_id)
        form = BaixaEncomendaForm()
        return render(request, 'encomenda.html', {'encomenda':encomenda,'form': form})


def encomendas_entregues(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    encomendas = Encomenda.objects.filter(data_hora_entrega != None)
    context = {'encomendas': encomendas}
    return render(request, 'encomendas_entregues.html', context)

def minhas_encomendas(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    # encomendas = Encomenda.objects.filter(morador=request.user)  precisa arrumar!!!!!!!
    encomendas = Encomenda.objects.all().order_by('data_hora_recebimento').reverse()
    moradores = Morador.objects.all()
    context = {'encomendas': encomendas, 'moradores': moradores}
    return render(request, 'minhas_encomendas.html', context)

def cadastrar_funcionario(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            msg_sucesso = f'Funcionário "{form.instance.nomeF}" cadastrado com sucesso!'
            form = FuncionarioForm()
            return render(request, 'cadastrar_funcionario.html', {'msg': msg_sucesso, 'form': form})
    else:
        form = FuncionarioForm()
    return render(request, 'cadastrar_funcionario.html', {'form': form})


def cadastrar_condominio(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    if request.method == 'POST':
        form = CondominioForm(request.POST)
        if form.is_valid():
            form.save()
            msg_sucesso = f'Condominio "{form.instance.nome}" cadastrado com sucesso!'
            form = CondominioForm()
            return render(request, 'cadastrar_condominio.html', {'msg': msg_sucesso, 'form': form})
    else:
        form = CondominioForm()
    return render(request, 'cadastrar_condominio.html', {'form': form})

def cadastrar_morador(request):
    if not request.user.is_authenticated:
        return redirect('index') # issue ---> precisa redirecionar para a página de login
    if request.method == 'POST':
        form = MoradorForm(request.POST)
        if form.is_valid():
            form.save()
            msg_sucesso = f'Morador "{form.instance.nome}" cadastrado com sucesso!'
            form = MoradorForm()
            return render(request, 'cadastrar_morador.html', {'msg': msg_sucesso, 'form': form})
    else:
        form = MoradorForm()
    return render(request, 'cadastrar_morador.html', {'form': form})
# cadastro de morador


def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    context = {'funcionarios': funcionarios}
    return render(request, 'lista_funcionarios.html', context)


#def login(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)
   #     if form.is_valid():
    #        user = form.save()
     #       login(request, user)
      #      return redirect('index')
    #else:
     #   form = UserCreationForm()
      #  return render(request, 'login.html', {'form': form})



"""
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
    #     if request.POST['username'] == 'admin' and request.POST['password'] == 'admin':
    #         return render(request, 'index.html')
    #     else:
    #         return render(request, 'login.html', {'msg': 'Usuário ou senha inválidos'})
    # return render(request, 'login.html')
"""



class LoginView(UserRegistrationForm):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid credentials'})

def logout_view(request):
    logout(request)
    return redirect('index')

def error404(request, exception):
    return redirect('index')
    
