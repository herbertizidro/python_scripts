import time

#script que edita códigos de N arquivos(da pasta em que se encontra). basta informar quais scripts e quais modificações, nesse caso
#se trata de um dicionário onde a chave é o trecho de código que deve ser modificado(nome de variável por exemplo) e o valor é a
#própria modificação
#esse script gera um log onde é registrado o índice da linha, o valor antes e depois da modificação, nome do arquivo
#e a data e hora da edição
#utilizo quando necessito modificar coisas simples/pequenas em alguns arquivos,
#ex: quando nomes de tabelas no banco de dados mudam, algo bem específico que
#eu sei que se eu rodar o script não irá provocar nenhum erro depois. "ESQUEMA.NOME_TABELA" ou "AMOSTRA_TABELA.feather"

def LOG(script, editado):
    data_hora = time.strftime('%d/%m/%Y - %H:%M:%S')
    with open("log-edita-scripts.txt", "a") as arq:
        arq.write("Arquivo: " + script + "\nModificações: \n")
        for linha in editado:
            arq.write(linha)
        arq.write("\nHora da modificação: " + data_hora + "\n\n")

def editaScripts(scripts, modificacoes):
    for script in scripts:
        with open(script, "r",) as arq:
            codigo = arq.readlines()
        codigo_editado = []
        nlinha = 1
        editado = []
        for linha in codigo:
            for chave in modificacoes:
                if chave in linha:
                    linha = linha.replace(chave, modificacoes[chave])
                    editado.append(str(nlinha) + " - " + chave + " -> " + modificacoes[chave] + "\n")
            codigo_editado.append(linha)
            nlinha += 1
        with open(script, "w") as arq:
            for linha in codigo_editado:
                arq.write(linha)
        if len(editado) > 0:
            print(script + " editado.")
        else:
            print(script + " não foi editado.")
        LOG(script, editado)


scripts = ["script1.R", "script2.R"]
modificacoes = {"EXEMPLO.csv":"EXEMPLO-ATUALIZADO.csv", "VARIAVELX":"VARIAVELX_ATUALIZADA"}
editaScripts(scripts, modificacoes)


#LOG exemplo:
'''
Arquivo: ocr_translate.py
Modificações: 
18 - ANTES -> DEPOIS
19 - ANTES -> DEPOIS
20 - ANTES -> DEPOIS
Hora da modificação: 12/06/2020 - 01:25:25

'''

