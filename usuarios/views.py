from django.shortcuts import render
from email import message
from django.shortcuts import render, redirect, get_object_or_404
from  django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome   = request.POST['nome'] #Pega as informações digitadas no cadastro
        email  = request.POST['email']
        senha  = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        
        if campo_vazio(email): #Se o campo email estiver em branco
            messages.error(request, 'O campo email não pode estar vazio')
            return redirect('cadastro')

        if campo_vazio(senha): #Se o campo senha estiver em branco
            messages.error(request, 'O campo senha não pode estar vazio')
            return redirect('cadastro')

        if campo_vazio(senha2): #Se o campo senha de confirmação estiver em branco
            messages.error(request,'O campo de confirmação de senha não pode estar vazio')
            return redirect('cadastro')

        if senha != senha2: #Se as senhas são diferentes (normal e confirmação)
            messages.error(request,'Senha deve ser igual a senha de confirmação!')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists(): #Se o usuário já existe 
            messages.error(request,'Usuário já cadastrado no sistema!')
            return redirect('cadastro')

        #Cria o objeto e grava no banco
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        print('Usuário cadastrado com sucesso!')
        messages.success(request,'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email   = request.POST['email'] #Pega as informações digitadas no login
        senha   = request.POST['senha'] 

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request,'Os campos email e senha não podem ficar em branco!')
            return redirect('login')

        if User.objects.filter(email=email).exists(): #Se o usuário já existe 
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() #Busca o nome do usuário para a autenticação
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request,'Login realizado com sucesso!')
                return redirect('dashboard')

    return render(request,'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'usuarios/dashboard.html')
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()