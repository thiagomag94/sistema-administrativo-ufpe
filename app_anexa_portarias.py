
from ast import Try
import os
from time import sleep
from PyPDF2 import PdfFileMerger




def anexa_portaria():
    #FUNÇÕES
    erro = ' '
    conta_corrompido = 0
   
    

    def mostra_texto(texto):
        print(f'''
    ---------------------------------------
    {texto}
    ---------------------------------------
    ''')

    #pega usuario--------------------------------------------------------------------
    username = os.environ['USERNAME']


    # Lista arquivo em determinado diretório-----------------------------------
    lista_cartas = [a for a in os.listdir('upload/cartas') if a.endswith(".pdf")]
    lista_portarias = [a for a in os.listdir('upload\\portaria') if a.endswith(".pdf")]
    merger = PdfFileMerger(strict=False)
    lenght_cartas= len(lista_cartas)
    #INICIALIZA UM CONTADOR DE DOCUMENTOS ANEXADOS--------------------------------------------
    count_document = 0

    #ANEXA AS PORTARIAS------------------------------------------------------------------------
    for pdf in lista_cartas :

        #ABRE CARTA DE ANUENCIA QUE CONSTA NA LISTA
        path_carta = f'upload/cartas/{pdf}'
        merger.append(open(path_carta, 'rb'))
        
        merger.append(open(f'upload/portaria/{lista_portarias[0]}', 'rb'))
        #merger.append(open(f'C:\\Users\\{username}\\Downloads\\Portaria n.º 5070-21 - delegacao de poderes amplos pesquisa e inovacao.pdf', 'rb'))
        
        try: 
            #SALVA E RENOMEA O ARQUIVO ANEXADO-----------------------------------------------
            with open(path_carta, "wb") as fout:
                merger.write(fout)
            merger.close()
            count_document+= 1
            texto = f'Documento {count_document} foi anexado com sucesso'
            #EXIBE NA TELA UMA CONFIRMAÇÃO DE DOCUMENTO ANEXADO
            mostra_texto( f'Documento {count_document} foi anexado com sucesso')
            #FALA TEXTO
        
            

            #REINICIALIZA O ARQUIVO PARA NOVA ANEXAÇÃO
            merger = PdfFileMerger(strict=False)
            sleep(0.5)
            
        except:
            erro = 'Arquivo corrompido'
            print(erro)   
            conta_corrompido = conta_corrompido + 1
            

    #MOSTRA FIM DE ARQUIVO
    mostra_texto('Process ended with success')

    #Apaga portaria de pasta
    for i in range(len(lista_portarias)):
        os.remove(f'upload/portaria/{lista_portarias[i]}')
    
    return conta_corrompido
    

if __name__ == '__main__':
    anexa_portaria()