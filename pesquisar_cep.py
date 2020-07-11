
#from busca_cep import BuscaCep
#cep = BuscaCep(<cep_que_você_quer_consultar>)
#print(cep.info())
#retorna uma lista com cep, logradouro, complemento, bairro, localidade e uf
#obter somente o bairro: print(cep.info()[3])
#a consulta é realizada no site https://viacep.com.br/

if __name__ != "__main__":

    class BuscaCep:
        def __init__(self, cep):
            self.cep = str(cep)

        def info(self) -> str:
            if len(self.cep) != 8:
                raise CepFormatoErro
            else:
                try:
                    import requests            
                    requisicao = requests.get("https://viacep.com.br/ws/{}/json/".format(self.cep))
                    info = requisicao.json()
                    return [info["cep"], info["logradouro"], info["complemento"], info["bairro"], info["localidade"], info["uf"]]
                
                except KeyError:
                    raise CepConsultaErro
                
                except requests.exceptions.ConnectionError:
                    raise CepConexaoErro


    #principais exceções
    class CepFormatoErro(Exception):
        def __str__(self):
            return "o cep precisa ter 8 dígitos."

    class CepConsultaErro(Exception):
        def __str__(self):
            return "o cep informado não foi encontrado."

    class CepConexaoErro(Exception):
        def __str__(self):
            return "sem conexão com a internet."
