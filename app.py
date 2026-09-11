from flask import Flask
from src.main import gerar_ranking

app = Flask(__name__)

@app.route('/')
def home():
    resultados = gerar_ranking()
    return str(resultados)

if __name__ == '__main__':
    app.run(debug=True)