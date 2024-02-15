from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/list", methods=['GET'])
def listar_itens():
    item = pd.read_csv('Lista.csv')
    produtos = item.to_dict('records')
    return render_template("produtos.html", lista_produtos=produtos)
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")