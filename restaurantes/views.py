from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Restaurantes
from django.contrib import auth, messages
from restaurantes.models import Restaurantes
from  django.contrib.auth.models import User

def index(request):
    restaurantes = Restaurantes.objects.all

    dados = {
        'restaurantes' : restaurantes
    }

    return render(request,'index.html',dados)

def cadastro(request):
    if request.method == 'POST':
        nome   = request.POST['nome'] #Pega as informações digitadas no cadastro
        endereco  = request.POST['endereco']
        cnpj  = request.POST['cnpj']
        #imagem  = request.POST['imagem']
        descricao  = request.POST['descricao']
        telefone  = request.POST['telefone']
        senha  = request.POST['password']
        senha2 = request.POST['password2']    
        
        #Validações para o cadastro
        if campo_vazio(nome): #Se o campo nome estiver em branco
            messages.error(request, 'O campo nome não pode estar vazio')
            return redirect('cadastro')

        if campo_vazio(endereco): #Se o campo email estiver em branco
            messages.error(request, 'O campo email não pode estar vazio')
            return redirect('cadastro')

        if campo_vazio(cnpj): #Se o campo senha estiver em branco
            messages.error(request, 'O campo cnpj não pode estar vazio')
            return redirect('cadastro')

        if campo_vazio(descricao): 
            messages.error(request, 'O campo descricao não pode estar vazio')
            return redirect('cadastro')
        
        if campo_vazio(telefone):
            messages.error(request, 'O campo telefone não pode estar vazio')
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

        if Restaurantes.objects.filter(cnpj=cnpj).exists(): #Se o usuário já existe 
            messages.error(request,'Restaurante já cadastrado no sistema!')
            return redirect('cadastro')

        if Restaurantes.objects.filter(nome=nome).exists(): #Se o usuário já existe 
            messages.error(request,'Restaurante já cadastrado no sistema!')
            return redirect('cadastro')

        #Cria o objeto e grava no banco
        restaurante = Restaurantes.objects.create(nome=nome, endereco=endereco, senha=senha,cnpj=cnpj,descricao=descricao,telefone=telefone)
        restaurante.save()
        user = User.objects.create_user(username=nome, email=cnpj, password=senha)
        user.save()
        print('Restaurante cadastrado com sucesso!')
        messages.success(request,'Restaurante cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request,'restaurante/cadastro.html')

def login(request):
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        senha = request.POST['password']

        if campo_vazio(cnpj):
            messages.error(request, 'O campo cnpj não pode estar vazio')
            return redirect('login')
        
        if campo_vazio(senha):
            messages.error(request, 'O campo senha não pode estar vazio')
            return redirect('login')
        
        if Restaurantes.objects.filter(cnpj=cnpj).exists(): #Se o usuário já existe 
            nome = Restaurantes.objects.filter(cnpj=cnpj).values_list('cnpj', flat=True).get() #Busca o nome do usuário para a autenticação
            user = Restaurantes.authenticate(request, username=nome, password=senha,email=cnpj)
            if user is not None:
                auth.login(request, user)
                messages.success(request,'Login realizado com sucesso!')
                #return redirect('dashboard')
                print("Login realizado com sucesso!")
                return 0

    else:
        return render(request,'restaurante/login.html')
def campo_vazio(campo):
    return not campo.strip()