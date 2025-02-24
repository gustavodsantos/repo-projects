# Projetos Web - Gustavo Junior Dos Santos

Este repositório contém uma coleção de projetos web desenvolvidos por Gustavo Junior Dos Santos, utilizando Django e outras tecnologias modernas.

## 🚀 Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Django 5.1.5, PostgreSQL
- **Ferramentas**: Docker, Nginx, Gunicorn, Poetry
- **CI/CD**: GitHub Actions
- **Outras**: Python 3.12, dj-database-url, python-decouple

## 📂 Estrutura do Projeto

O repositório está organizado em diferentes apps Django, cada uma com funcionalidades específicas:

- **base**: Funcionalidades básicas como autenticação, páginas estáticas e gerador de senhas
- **cursos**: Gerenciamento e exibição de cursos
- **quiz**: Sistema de quiz com classificação
- **tarefas**: Gerenciamento de tarefas (TODO)

## 🛠️ Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.12
- Poetry (para gerenciamento de dependências)

### Usando Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/gustavodsantos/repo-projects.git
   cd repo-projects
   ```

2. Crie o arquivo `.env` com as variáveis de ambiente necessárias:
   ```bash
   cp .env.example .env
   ```

3. Inicie os containers:
   ```bash
   docker-compose up --build
   ```

4. Acesse a aplicação em: http://localhost

### Desenvolvimento Local

1. Instale as dependências:
   ```bash
   poetry install
   ```

2. Configure o banco de dados PostgreSQL

3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## 🧪 Testes

Para executar os testes:

    ```bash
    poetry run pytest mysite --cov=mysite --cov-fail-under=60
    ```

## 🌐 Funcionalidades Principais

- **Autenticação de Usuários**: Registro, login e alteração de senha
- **Gerador de Senhas**: Gera senhas seguras com diferentes critérios
- **Sistema de Cursos**: Exibição e detalhes de cursos
- **Quiz**: Sistema de perguntas e respostas com classificação
- **Lista de Tarefas**: Gerenciamento básico de tarefas

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📬 Contato

- **GitHub**: [@gustavodsantos](https://github.com/gustavodsantos)
- **LinkedIn**: [Gustavo Junior Dos Santos](https://www.linkedin.com/in/gustavo-junior-dos-santos/)
- **E-mail**: gustavojuniordos@hotmail.com
- **Telefone**: +55 43 99619-5504

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
