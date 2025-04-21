

# Projeto IA - Assistente Dinâmico

Este é um projeto de assistente de IA dinâmico que responde a perguntas de forma clara e objetiva, utilizando Markdown para formatar as respostas. Ele suporta exibição em tempo real, semelhante ao ChatGPT.

---

## 📖 Introdução

O projeto utiliza Flask como framework web e Flask-SocketIO para comunicação em tempo real. Ele também integra a biblioteca `ollama` para geração de respostas baseadas em IA. O objetivo é criar uma interface interativa e responsiva para responder a perguntas de forma dinâmica.

---

## 🛠️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:

- **Python 3.8 ou superior**: Certifique-se de que o Python está instalado e configurado no PATH.
- **Pip**: O gerenciador de pacotes do Python.
- **Virtualenv (opcional)**: Para criar um ambiente virtual isolado.

---

## 📦 Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o servidor**:
   ```bash
   python app.py
   ```

5. **Acesse a aplicação no navegador**:
   - Abra o navegador e vá para: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📋 Dependências (requirements.txt)

Aqui estão as dependências necessárias para o projeto, que devem ser listadas no arquivo `requirements.txt`:

```
flask
flask-socketio
ollama
markdown
```

Para gerar o arquivo `requirements.txt` automaticamente, você pode usar o comando:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Funcionalidades

- Respostas dinâmicas e formatadas em Markdown.
- Exibição em tempo real das respostas.
- Suporte a blocos de código, listas e formatação avançada.
- Cache de respostas para melhorar o desempenho.

---

## 🛠️ Estrutura do Projeto

```
.
├── app.py                  # Arquivo principal do servidor Flask
├── templates/
│   └── index.html          # Interface do usuário
├── static/
│   └── styles.css          # Arquivo de estilos (opcional)
├── config/
│   └── agent_profiles.json # Configuração de agentes (não usado no modelo dinâmico)
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

## 🧪 Testes

Para testar o projeto, faça perguntas no campo de entrada e veja as respostas sendo exibidas em tempo real. Exemplos de perguntas:

- "Me dê um código de Hello World em Python."
- "Explique o que é Flask."
- "Como criar uma função em JavaScript?"

---

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT). Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

---

## 💡 Dicas

- Certifique-se de que a porta `5000` não está sendo usada por outro processo.
- Use um ambiente virtual para evitar conflitos de dependências.
- Para produção, utilize um servidor WSGI como `gunicorn` ou `waitress`.

---

Com este `README.md`, você terá uma documentação clara e organizada para o seu projeto. Certifique-se de ajustar os detalhes, como o link do repositório, conforme necessário.---

## 🧪 Testes

Para testar o projeto, faça perguntas no campo de entrada e veja as respostas sendo exibidas em tempo real. Exemplos de perguntas:

- "Me dê um código de Hello World em Python."
- "ique o que é Flask."
- "Como criar uma função em JavaScript?"

---

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT). Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

---

## 💡 Dicas

- Certifique-se de que a porta `5000` não está sendo usada por outro processo.
- Use um ambiente virtual para evitar conflitos de dependências.
- Para produção, utilize um servidor WSGI como `gunicorn` ou `waitress`.

---

