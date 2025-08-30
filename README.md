# Entrega A2

Este projeto contém uma aplicação que utiliza um banco de dados. Siga os passos abaixo para executar corretamente:

## Instalação

1. **Instale o Django:**
    ```bash
    python -m pip install Django
    ```
    
2. **Crie um super usuário para adicionar e remover categorias e produtos:**
    ```bash
    python manage.py createsuperuser
    ```

3. **Crie as migrações do banco de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Inicie a aplicação:**
    ```bash
    python manage.py runserver
    ```

5. **Execute os testes:**
    ```
    Dentro da aplicação, acesse o /admin/ com seu super usuário, testando funcionalidades como:
    - Criação de Categoria;
    - Criação de Produto;

    Após isso, pode acessar a /loja/ e realizar os testes como:
    - Adicionar produtos ao carrinho;
    - Visualizar itens no carrinho;
    - Remover produtos do carrinho;
    ```

## Colaboradores

- Barbara Borges Woitas - RGM 28927940
- João Arthur Barp Begnini - RGM 29462860

---