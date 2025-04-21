from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
import ollama
import markdown

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Altere isso para produção
socketio = SocketIO(app)

# registra um filtro chamado "md" que converte Markdown em HTML
app.jinja_env.filters['md'] = lambda text: markdown.markdown(
    text or "", 
    extensions=['fenced_code']
)

# 1) Warm-up para “carregar” o modelo na memória
try:
    ollama.generate(model="mistral", prompt="Escreva uma pequena frase de exemplo em Markdown com código Python.")  
except Exception:
    pass

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    return render_template("index.html", chat_history=session.get("chat_history", []))

# WebSocket para geração de resposta em tempo real com stream
@socketio.on('generate_response')
def handle_generate_response(data):
    query = data.get('query')

    try:
        stream = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": query}],
            stream=True
        )

        for chunk in stream:
            content = chunk.get("message", {}).get("content", "")
            if content:
                emit('response_chunk', {'chunk': content})
    except Exception as e:
        emit('response_chunk', {'chunk': f"Erro: {e}"})
    emit('response_done')

@app.route("/clear_cache", methods=["POST"])
def clear_cache():
    # Removido uso do LRU cache para permitir resposta em tempo real
    return "Cache limpo com sucesso!", 200

if __name__ == "__main__":
    socketio.run(app, debug=True)
