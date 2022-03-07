class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        return print(f"\nCC Nº {self.numero}\nSaldo: R${self.saldo:,.2f}\n")

    def saque(self, valor):
        if self.valor >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print(f"\nValor Requisitado: R${valor:,.2f}\nValor Disponível: R${self.saldo:,.2f}\n")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f"\nExtrato CC Nº {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}\n")
        print(f"\n\tSaldo: R${self.saldo:,.2f}\n")        

class ContaEspecial(Conta):

    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo=0)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print(f"\nValor Requisitado: R${valor:,.2f}\nValor Disponível: R${self.saldo:,.2f}\n")            

class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abrir_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()            
