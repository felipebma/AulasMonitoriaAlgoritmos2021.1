class Aluno:

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
        self.nota1 = None
        self.nota2 = None
        self.nota3 = None

    def inicializar_nota(self, nota: float, numero_prova: int):
        if numero_prova == 1:
            self.nota1 = nota
        elif numero_prova == 2:
            self.nota2 = nota
        elif numero_prova == 3:
            self.nota3 = nota
        else:
            print("Numero prova inválido")


    def verifica_situacao_media(self) -> bool:
        if self.nota1 == None or self.nota2 == None or self.nota2 == None:
            print("Uma das notas não foi inicializada")
            return False
        media = (self.nota1 + self.nota2 + self.nota3)/3
        return media >= 7

    def imprime_informacoes(self):
        print("nome: {}".format(self.nome))
        print("cpf: {}".format(self.cpf))
        print("nota 1: {}".format(self.nota1))
        print("nota 2: {}".format(self.nota2))
        print("nota 3: {}".format(self.nota3))


aluno = Aluno("123456789", "Felipe")
aluno.inicializar_nota(10, 1)
aluno.inicializar_nota(3, 2)
aluno.inicializar_nota(8, 3)
aluno.imprime_informacoes()
print(aluno.verifica_situacao_media())

