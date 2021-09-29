from abc import ABC, abstractmethod

class Empreendimento(ABC):

    def __init__(self, nome) -> None:
        self.nome = nome  
        self.endereco = None
        self.CNPJ = None

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getCNPJ(self):
        return self.CNPJ
    
    def setCNPJ(self, cnpj):
        self.CNPJ = cnpj
    
    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self, endereco):
        self.endereco = endereco   
    
    @abstractmethod
    def getLucro(self):
        pass
    
    @abstractmethod
    def setVenda(self, venda):
        pass

class Supermercado(Empreendimento):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.lucro = 0     

    def getLucro(self):
        return self.lucro
    
    def setVenda(self, venda: float):
        self.lucro += venda

    def __str__(self):
        return "nome: {}\ncnpj: {}\nendereço: {}\nlucro: {}".format(self.nome, self.CNPJ, self.endereco, self.lucro)


# Inicialize 3 objetos do tipo Supermercado: VarejaoCIn, CompraUFPE e
# EstudantesVarzea. Peça para o usuário fornecer as informações
# iniciais e depois pergunte se houve alguma venda para cada um dos
# supermercados. Encerre imprimindo as informações gerais dos
# supermercados.

def pega_informacoes(supermercado: Supermercado):
    supermercado.setCNPJ(input("Digite o CNPJ do {}: ".format(supermercado.getNome())))
    supermercado.setEndereco(input("Digite o Endereço do {}: ".format(supermercado.getNome())))

varejaoCIN = Supermercado("Varejão CIN")
compraUFPE = Supermercado("Compra UFPE")
estudantesVarzea = Supermercado("Estudantes Varzea")

pega_informacoes(varejaoCIN)
pega_informacoes(compraUFPE)
pega_informacoes(estudantesVarzea)

print(varejaoCIN, end="\n\n")
print(compraUFPE, end="\n\n")
print(estudantesVarzea)
