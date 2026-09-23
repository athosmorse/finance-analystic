from flask import Flask, render_template, request
from src.main import gerar_ranking
from src.main import ordenar_ranking

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ranking')
def ranking():
    resultados = gerar_ranking()
    campo = request.args.get('campo', None) # se não vier nada, usa None como padrão
    ordem = request.args.get('ordem', None) # se não vier nada, usa None como padrão
    resultados_ordenados = ordenar_ranking(resultados, campo, ordem)
    return render_template('ranking.html', resultados=resultados_ordenados, campo=campo, ordem=ordem)

if __name__ == '__main__':
    app.run(debug=True)