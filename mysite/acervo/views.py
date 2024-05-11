from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from .models import Item, Livro, Contato, Emprestimo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# LOGIN E LOGOUT

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acervo/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            contexto = {'erro': 'Usuário ou senha inválidos!'}
            return render(request, 'acervo/login.html', contexto)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acervo/cadastro.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['senha']
        first_name = request.POST['nome']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            contexto = {'erro': 'Este username já existe!'}
            return render(request, 'acervo/cadastro.html', contexto)

        user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
        user.save()
        return redirect('/')
    
# HOME E PESQUISAR

@method_decorator(login_required, name='dispatch')
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        lista_itens = Item.objects.filter(user = user).order_by('nome')
        lista_livros = Livro.objects.filter(user = user).order_by('titulo')
        lista_contatos = Contato.objects.filter(user=user).order_by('nome_cont')
        lista_emp = Emprestimo.objects.filter(user=user, data_dev = None)
        emprestimos_cadastrados = lista_emp.count() > 0
        contexto = {
            'user': user,
            'lista_itens': lista_itens,
            'lista_livros': lista_livros,
            'lista_contatos': lista_contatos,
            'lista_emp': lista_emp,
            'emprestimos_cadastrados': emprestimos_cadastrados,
            }
        return render(request, 'acervo/home.html', contexto)
    
class PesquisarView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        pesquisa = request.GET.get('pesquisa')
        lista_itens = Item.objects.filter(nome__icontains = pesquisa, user = user)
        lista_livros = Livro.objects.filter(titulo__icontains = pesquisa, user = user)
        lista_contatos = Contato.objects.filter(nome_cont__icontains = pesquisa, user = user)
        contexto = {
            'lista_itens': lista_itens,
            'lista_livros': lista_livros,
            'lista_contatos': lista_contatos,
            'pesquisa':pesquisa
            }
        return render(request, 'acervo/pesquisa.html', contexto )
    
# ITEM

class SaveItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acervo/item.html', {'user': request.user})

    def post(self, request, *args, **kwargs):
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        item = Item.objects.create(
            nome = nome,
            descricao = descricao,
            emprestado = False,
            user = request.user
        )
        item.save()
        return redirect('/home/')

class EditarItemView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        item = Item.objects.get(pk = kwargs['pk'])
        return render(request, 'acervo/item_detalhes.html', {'item':item, 'user':user})

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk = kwargs['pk'])
        nome = request.POST['nome']
        descricao = request.POST['descricao']

        Item.objects.filter(pk = item.pk).update(nome = nome, descricao = descricao)
        return redirect('/home/')

class DeleteItemView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk = kwargs['pk'])
        item.delete()
        return redirect('/home/')
    
# LIVRO

class SaveLivroView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acervo/livro.html', {'user':request.user})

    def post(self, request, *args, **kwargs):
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        ano = request.POST['ano']
        livro = Livro.objects.create(
            titulo = titulo,
            autor = autor,
            ano = ano,
            emprestado = False,
            user = request.user
        )
        livro.save()
        return redirect('/home/')

class EditarLivroView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        livro = Livro.objects.get(pk = kwargs['pk'])
        return render(request, 'acervo/livro_detalhes.html', {'livro':livro, 'user':user})

    def post(self, request, *args, **kwargs):
        livro = Livro.objects.get(pk = kwargs['pk'])
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        ano = request.POST['ano']

        Livro.objects.filter(pk = livro.pk).update(titulo = titulo, autor = autor, ano = ano)
        return redirect('/home/')

class DeleteLivroView(View):
    def get(self, request, *args, **kwargs):
        livro = Livro.objects.get(pk = kwargs['pk'])
        livro.delete()
        return redirect('/home/')
    
# CONTATO

class SaveContatoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acervo/contato.html', {'user':request.user})

    def post(self, request, *args, **kwargs):
        nome_cont = request.POST['nome_cont']
        email = request.POST['email']
        telefone = request.POST['telefone']
        contato = Contato.objects.create(
            nome_cont = nome_cont,
            email = email,
            telefone = telefone,
            user = request.user
        )
        contato.save()
        return redirect('/home/')

class EditarContatoView(View):
    def get(self, request, *args, **kwargs):
        contato = Contato.objects.get(pk = kwargs['pk'])
        user = request.user
        return render(request, 'acervo/contato_detalhes.html', {'contato':contato, 'user':user})

    def post(self, request, *args, **kwargs):
        contato = Contato.objects.get(pk = kwargs['pk'])
        nome_cont = request.POST['nome_cont']
        email = request.POST['email']
        telefone = request.POST['telefone']

        Contato.objects.filter(pk = contato.pk).update(nome_cont = nome_cont, email = email, telefone = telefone, user = request.user)
        return redirect('/home/')

class DeleteContatoView(View):
    def get(self, request, *args, **kwargs):
        contato = Contato.objects.get(pk = kwargs['pk'])
        contato.delete()
        return redirect('/home/')
    
# EMPRÉSTIMO

class EmprestimoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        lista_itens = Item.objects.filter(user = user).order_by('nome')
        lista_livros = Livro.objects.filter(user = user).order_by('titulo')
        lista_contatos = Contato.objects.filter(user = user).order_by('nome_cont')

        contexto = {
            'lista_itens':lista_itens,
            'lista_livros':lista_livros,
            'lista_contatos':lista_contatos,
            'user':user,
        }
        return render(request, 'acervo/emprestimo.html', contexto)

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item')
        livro_id = request.POST.get('livro')
        contato_id = request.POST.get('contato')

        if contato_id:
            contato = Contato.objects.get(id=contato_id)

        with transaction.atomic():
            if item_id == 'Selecionar item':
                item = None
            else:
                item = Item.objects.get(id = item_id)
                item.emprestado = True
                item.save()

            if livro_id == 'Selecionar livro':
                livro = None
            else:
                livro = Livro.objects.get(id = livro_id)
                livro.emprestado = True
                livro.save()

            emp = Emprestimo.objects.create(
                contato = contato,
                livro = livro,
                item = item,
                user = request.user
            )
            emp.save()

            if item:
                item.save()
            if livro:
                livro.save()

        return redirect('/home/')

class EmprestimoFinalizarView(View):
    def get(self, request, *args, **kwargs):
        emp = Emprestimo.objects.get(pk = kwargs['pk'])
        emp.data_dev = date.today()

        livro = emp.livro
        if livro:
            livro.emprestado = False
            livro.save()

        item = emp.item
        if item:
            item.emprestado = False
            item.save()

        emp.save()

        return redirect('/home/')

class RegistroEmprestimoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        lista_emp = Emprestimo.objects.filter(user = user, data_dev__isnull = False)
        emprestimos_finalizados = lista_emp.exists()
        contexto = {'lista_emp': lista_emp, 'user': user, 'emprestimos_finalizados': emprestimos_finalizados}
        return render(request, 'acervo/registro_emprestimo.html', contexto)