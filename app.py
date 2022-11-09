from flask import Flask
import flask
from flask import render_template, request
import os
import pandas as pd
from werkzeug.utils import secure_filename
from app_anexa_portarias import anexa_portaria
import time
from app_cria_documentos import cria_documento

app = Flask(__name__, template_folder='templates', static_folder='static')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload\cartas')
UPLOAD_FOLDER_PORTARIA = os.path.join(os.getcwd(), 'upload\portaria')



@app.route('/pdf')
def homepage():
       
    return render_template("anexarportarias.html" )

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])

def upload():
    if flask.request.method == "POST":

        
        cartas = flask.request.files.getlist('cartas')
        
        conta_carta = 0
        for carta in cartas:
            print(carta.filename)
            print('---------------------')
            savePath_carta = os.path.join(UPLOAD_FOLDER, secure_filename(carta.filename))
            carta.save(savePath_carta)
            conta_carta += 1

        portarias = flask.request.files.getlist('portaria')
        for portaria in portarias:
            savePath_portaria = os.path.join(UPLOAD_FOLDER_PORTARIA, secure_filename(portaria.filename))
            portaria.save(savePath_portaria)
      
        if conta_carta == 1:

            return render_template("anexarportarias.html", erro= f"Carta enviada" )

        else:
            return render_template("anexarportarias.html", erro= f"{conta_carta} cartas enviadas" )

        
@app.route('/anexa', methods=['POST'])

def anexa():
    if flask.request.method == "POST":
        try:
            erro = anexa_portaria()
            anexa_portaria()
        except IndexError:
            pass

        finally:
            if (erro > 0):

                return render_template("anexarportarias.html", upload= f"As cartas foram anexadas com portaria escolhida, {erro} arquivo corrompido" )
            
            else:
                return render_template("anexarportarias.html", upload= f"As cartas foram anexadas com portaria escolhida")




@app.route('/cartas')
def pagina_cartas():
    return render_template('cartas.html')





@app.route('/criacartas', methods=['GET', 'POST'])

def cria_cartas():
    if flask.request.method == "POST":
        projeto = request.form['titulo_projeto']
        edital= flask.request.form['edital']
        coordenador= flask.request.form['coordenador']
        siape = flask.request.form['siape']
        lotacao = flask.request.form['lotação']

        planilha = pd.read_excel('DATABASE\database.xlsx')
        lista = [projeto, edital, coordenador, siape, lotacao]
        print(lista)

        planilha.loc[planilha.shape[0]] = lista
        
        with pd.ExcelWriter('DATABASE\database.xlsx', mode="a", engine="openpyxl",  if_sheet_exists="replace") as writer:
            planilha.to_excel(writer , sheet_name = 'database', index=False)
        
        
        cria_documento()

        return render_template("cartas.html", criou_carta = f"As cartas foram criadas")
    else:
        return render_template("cartas.html", criou_carta = f"As cartas não foram criadas")
       

if __name__ == "__main__" :
    app.run(debug=False)