from docx import Document
from datetime import datetime
from translate import Translator
import pandas as pd
from unidecode import unidecode
from docxtpl import DocxTemplate


def cria_documento():
    # inicializa tradutor que será necessário para traduzir o mês por extenso para PT-BR
    tradutor = Translator(from_lang ="english", to_lang= "pt-br")
    tabela = pd.read_excel('DATABASE\database.xlsx')

    for linha in tabela.index: 

        item1 =  tabela.loc[linha, "TITULO"]
        item2 =  tabela.loc[linha, "EDITAL"]
        item3 =  tabela.loc[linha, "COORDENADOR"]
        item4 =  tabela.loc[linha, "SIAPE"]
        item5 =  tabela.loc[linha, "LOTAÇÃO"]
        dia = str(datetime.now().day)
        mes = datetime.now()
        mes = mes.strftime("%B")
        mes_traduzido = tradutor.translate(str(mes))


        ano = str(datetime.now().year)


        ####abre documento1 com python-docx

        #documento = Document("MODELO\modelo.docx")
        #paragrafos = documento.paragraphs

    
        for orgao in ["FACEPE", "Facepe", "facepe"]:
            if orgao in item2:
                print("------------------------------------------------------------------------")
                print(item2)
                print("------------------------------------------------------------------------")
            #seta cabeçalho de acordo com o orgão de fomento
                cabecalho = "À Fundação de Amparo à Ciência e Tecnologia de Pernambuco - FACEPE"
                #CONFIGURA DICIONARIO QUE SERÁ INSERIDO NO DOCUMENTO
                referencias = {
                    "CABECALHO": cabecalho,
                    "TITULO_PROJETO": item1,
                    "NOME_EDITAL": item2,
                    "NOME_COORDENADOR": item3,
                    "NUMERO_SIAPE": item4,
                    "NOME_DEPARTAMENTO": item5,
                    "DATA": dia,
                    "MES" : mes_traduzido,
                    "ANO" : ano,
                }
            
                #for p in paragrafos:
                    ##for codigo in referencias:
                        #valor = referencias[codigo]
                        #p.text= p.text.replace(codigo, str(valor))

                #-------------Abre template com docxtpl (alternativa à outra biblioteca)------
                documento = DocxTemplate("MODELO\modelo.docx") 
                documento.render(referencias)
                print("------------------------------------------------------------------------")
                print(item3)  
                print("------------------------------------------------------------------------") 
                nome_doc = 'CARTA DE ANUENCIA - '+item2+'- '+item3+'.docx'
                nome_doc_novo =  nome_doc.replace("/", "_")
                documento.save(nome_doc_novo)
        
        for orgao in ["CNPq", "cnpq", "CNPQ"]:
            if orgao in item2:
                print("------------------------------------------------------------------------")
                print(item2)
                cabecalho = '''Ao Conselho Nacional de Desenvolvimento Científico e Tecnológico – CNPq,
Ministério da Ciência, Tecnologia e Inovações – MCTI'''
                #CONFIGURA DICIONARIO QUE SERÁ INSERIDO NO DOCUMENTO
                referencias = {
                    "CABECALHO": cabecalho,
                    "TITULO_PROJETO": item1,
                    "NOME_EDITAL": item2,
                    "NOME_COORDENADOR": item3,
                    "NUMERO_SIAPE": item4,
                    "NOME_DEPARTAMENTO": item5,
                    "DATA": dia,
                    "MES" : mes_traduzido,
                    "ANO" : ano,
                }

              
                documento = DocxTemplate("MODELO\modelo.docx") 
                documento.render(referencias)
                print("-------------------------------------------------")    
                print(item3)   
                nome_doc = 'CARTA DE ANUENCIA - '+item2+'- '+item3+'.docx'
                nome_doc_novo =  nome_doc.replace("/", "_")
                documento.save(nome_doc_novo)

if __name__ == '__main__':
    cria_documento()