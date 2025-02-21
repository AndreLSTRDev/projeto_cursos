# README - Plataforma de Cursos Online

Este projeto consiste em uma plataforma de cursos online desenvolvida com Django, um framework web em Python. A plataforma oferece funcionalidades como cadastro de cursos, aulas, professores, matrículas de alunos, acompanhamento de progresso e emissão de certificados (opcional).

## Funcionalidades

### Cursos:

1.  **Cadastro de cursos:** Permite cadastrar cursos com nome, descrição, carga horária, categoria, nível, requisitos, data de início, instrutores, alunos matriculados, materiais e preço.
2.  **Listagem de cursos:** Exibe uma lista de cursos com paginação, filtros e ordenação.
3.  **Visualização detalhada de cursos:** Permite visualizar informações detalhadas de cada curso.

### Aulas:

1.  **Cadastro de aulas:** Permite cadastrar aulas com título, descrição, duração, vídeo, materiais, ordem e tipo (vídeo, texto, exercício, link externo).

### Professores:

1.  **Cadastro de professores:** Permite cadastrar professores com nome, formação, experiência, mini currículo, foto, biografia, áreas de interesse e contato.

### Alunos:

1.  **Modelo de aluno:** Utiliza o modelo de usuário padrão do Django, com campos extras como nome, email e data de nascimento.

### Matrículas:

1.  **Matrícula de alunos:** Permite que alunos se matriculem em cursos.
2.  **Gerenciamento de matrículas:** Permite gerenciar matrículas com status (ativo, inativo, concluído).

### Progresso:

1.  **Acompanhamento de progresso:** Permite acompanhar o progresso dos alunos em cada aula (aulas concluídas, notas em exercícios, etc.).

### Certificados (opcional):

1.  **Geração de certificados:** Permite gerar automaticamente certificados em PDF para alunos que concluem cursos.

### Funcionalidades extras (em desenvolvimento):

1.  **Sistema de avaliação:** Permite avaliar cursos e professores.
2.  **Fóruns de discussão:** Cria fóruns de discussão para cada curso.
3.  **Sistema de mensagens:** Permite trocar mensagens entre alunos e professores.

## Tecnologias utilizadas

*   Python
*   Django
*   Banco de dados PostgreSQL (padrão do Django)
*   Biblioteca fpdf (opcional, para geração de certificados em PDF)

## Configuração do ambiente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/plataforma_cursos.git](https://github.com/seu-usuario/plataforma_cursos.git)
    ```

2.  **Crie um ambiente virtual:**
    ```bash
    python3 -m venv .venv
    ```

3.  **Ative o ambiente virtual:**
    ```bash
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate  # Windows
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Crie o banco de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Crie um usuário superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

## Execução do projeto

1.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

2.  **Acesse o painel administrativo:** Acesse `http://127.0.0.1:8000/admin/` e faça login com o usuário superusuário criado.

3.  **Acesse a plataforma:** Acesse `http://127.0.0.1:8000/cursos/`.

## Próximos passos

1.  Implementar as funcionalidades extras (sistema de avaliação, fóruns, mensagens, certificados).
2.  Criar templates HTML para as páginas da plataforma.
3.  Adicionar testes unitários para garantir a qualidade do código.
4.  Implementar sistema de pagamento para matrículas.
5.  Publicar a plataforma em um servidor web.

## Contribuição

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está sob a licença MIT.

