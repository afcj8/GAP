<h1>GAP</h1>

<h2>⚡ Projeto</h2>
Durante a disciplina de Desenvolvimento Web no curso de Análise e Desenvolvimento de Sistemas do IFRN, foi proposto o desenvolvimento de um sistema para gerenciar o acervo bibliográfico pessoal de um usuário. Esse sistema permitirá que os usuários cadastrem seus livros (ou outros itens) pessoais, além de oferecer a funcionalidade de registrar empréstimos para contatos previamente cadastrados no sistema, assim como o registro das devoluções dos itens emprestados.
<hr>
O GAP (Gerenciamento de Acervo Pessoal) é um sistema inovador desenvolvido para ajudar os usuários a organizar e gerenciar seu acervo bibliográfico ou de outros itens pessoais. Com o GAP, os usuários podem cadastrar livros ou outros itens, realizar empréstimos para contatos cadastrados e registrar a devolução dos itens ou livros emprestados. A plataforma oferece uma interface intuitiva e de fácil utilização, permitindo uma gestão eficiente e conveniente do acervo pessoal.
<hr>
<img width="958" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/c5ae2479-3443-4eb7-8590-93996ce88213">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/b7bfb860-9d26-4185-b5bd-5fc20a752d88">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/5c13641e-318b-4bf3-90ed-fdbfcf912580">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/8f3e5719-4820-476b-8046-c12c98fff44b">
<img width="959" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/b0a7275c-68fd-4a35-85b9-d8bbd14225e7">
<img width="949" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/95130d99-e44f-4ee6-868c-828f4684bf38">
<img width="947" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/ef96a9bb-ce01-4674-bf80-b1de9364b6cb">
<img width="945" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/5e7c40f8-85ea-4bad-8fa3-7d5f93c0a24c">
<img width="948" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/4911f379-bc6c-44be-b658-b6ba5381ca8a">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/4f24947b-fbff-4623-909b-90c413937db1">
<img width="959" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/94423113-52c0-4af2-84a7-663d52d32bf2">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/32e8fa5f-4e31-4cee-99d1-61ed6d848d85">
<img width="959" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/46eea0a9-2fb3-4547-9eaa-91368a22fdcf">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/db030bbb-5b56-4946-9299-6dd1b38a36bb">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/c1a919b4-64e2-4dc4-9647-ba5ac71b3fbe">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/8e08a0aa-31b1-49d1-876f-55e226aaf381">
<img width="959" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/78303311-045a-4ff0-8bce-45e50a37cbf0">
<img width="959" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/0249f6d1-340c-49eb-941b-1823342d6b19">
<img width="960" alt="image" src="https://github.com/afcj8/GAP/assets/102259875/c1283a0e-2f49-4408-b5c4-645aad62c821">

<h2>🚀 Tecnologias</h2>

- [Django](https://docs.djangoproject.com/pt-br/4.2/)
- [Bootstrap](https://getbootstrap.com/)
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)


## 🛠️ Manual do Desenvolvedor (legado)

1. Clone o repositório:
   ```bash
   git clone https://github.com/afcj8/gap.git
   ```

2. Verifique se o Python está instalado em sua máquina:
   ```bash
   python --version
   ```

3. Navegue até o diretório clonado:
   ```bash
   cd mysite
   ```

4. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

5. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

6. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

7. Crie o banco de dados:
   ```bash
   python manage.py migrate
   ```

8. (Opcional) Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

9. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

10. Abra o navegador com a seguinte url:
   ```bash
   http://localhost:8000/
   ```