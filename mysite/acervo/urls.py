from django.urls import path
from . import views

app_name = 'acervo'
urlpatterns = [
    path('', views.LoginView.as_view(), name = 'login'),
    path('', views.LogoutView.as_view(), name = 'logout'),
    path('cadastro/', views.CadastroView.as_view(), name = 'cadastro'),
    path('home/', views.HomeView.as_view(), name = 'home'),
    path("home/pesquisar", views.PesquisarView.as_view(), name='pesquisa'),

    # urls dos itens

    path('home/salvar/item', views.SaveItemView.as_view(), name='salva_item'),
    path('<int:pk>/editar/item', views.EditarItemView.as_view(), name='item_detalhes'),
    path('<int:pk>/deletar/item', views.DeleteItemView.as_view(), name='deletar_item'),

    # urls dos livros

    path('home/salvar/livro', views.SaveLivroView.as_view(), name='salva_livro'),
    path('<int:pk>/editar/livro', views.EditarLivroView.as_view(), name='livro_detalhes'),
    path('<int:pk>/deletar/livro', views.DeleteLivroView.as_view(), name='deletar_livro'),

    # urls dos contatos

    path('home/salvar/contato', views.SaveContatoView.as_view(), name='salva_contato'),
    path('<int:pk>/editar/contato', views.EditarContatoView.as_view(), name='contato_detalhes'),
    path('<int:pk>/deletar/contato', views.DeleteContatoView.as_view(), name='deletar_contato'),

    # urls dos empréstimos

    path('home/salvar/emprestimo', views.EmprestimoView.as_view(), name='emprestimo'),
    path('<int:pk>/finalizar', views.EmprestimoFinalizarView.as_view(), name='finalizar'),
    path('home/registro', views.RegistroEmprestimoView.as_view(), name='registro_emprestimo'),
]