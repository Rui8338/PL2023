import re

class cabine:

    def __init__(self):
        self.saldo=0
        self.estado="INICIO"

    def estado(self):
        return(self.estado)

    def levantar(self,linha):
        if self.estado=="LEVANTAR":
            print("maq: Já levantou o telefone")
        else:
            self.estado="LEVANTAR"
        
    def moeda(self,linha):
        moedas=re.findall(r"\d+[e|c]",linha)

        moedasvalidas=["1c","2c","5c","10c", "20c", "50c", "1e", "2e"]
        moedasinvalidas=[]
        
        for moeda in moedas:
            if moeda in moedasvalidas:
                if moeda == "1c":
                    self.saldo += 0.01
                elif moeda == "2c":
                    self.saldo += 0.02
                elif moeda == "5c":
                    self.saldo += 0.05
                elif moeda == "10c":
                    self.saldo += 0.1
                elif moeda == "20c":
                    self.saldo += 0.2
                elif moeda == "50c":
                    self.saldo += 0.5
                elif moeda == "1e":
                    self.saldo += 1
                else:
                    self.saldo += 2
            else:
                moedasinvalidas.append(moeda)

        if moedasinvalidas != None:
            print(f"maq: Moeda {moedasinvalidas} inválida. Moedas aceites: 1c, 2c, 5c, 10c, 20c, 50c, 1e, 2e")
            print(f"maq: Saldo={self.saldo}")

    def abortar(self,linha):
        self.troco()
        self.saldo=0

    def telefonema(self,linha):
        numero = linha[2:]
    
        if re.match(r"00\d{9}",numero):
            if saldo >= 1.5:
                saldo -= 1.5
            else:
                print("maq: Saldo insuficiente para chamada internacional.")

        elif re.match(r"\d{9}",numero):
            if re.match(r"601", numero) or re.match(r"641", numero):
                print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")

            elif re.match(r"2", numero):
                if self.saldo >= 0.25:
                    self.saldo -= 0.25
                    print(f"maq: saldo = {self.saldo}")
                else:
                    print("maq: Saldo insuficiente para chamada nacional.")

            elif re.match(r"800", numero):
                None

            elif re.match(r"808", numero):
                if self.saldo >= 0.1:
                    self.saldo -= 0.1
                else:
                    print("maq: Saldo insuficiente para chamada azul.")
            else:
                print("maq: Número inválido")
        else:
            print("maq: Número inválido")
            

    def pousar(self,linha):
        self.troco()
        self.saldo=0

    def troco(self):
        troco = self.saldo
        moedas={200:0,
                100:0,
                50:0,
                20:0,
                10:0,
                5:0,
                2:0,
                1:0,
                }
        
        saldo1=self.saldo*100
        while saldo1>0:
            for moeda in [200, 100, 50, 20, 10, 5, 2, 1]:
                if saldo1 >= moeda:
                    moedas[moeda] += 1
                    saldo1 -= moeda
        self.saldo=0           
        print(f"troco: {moedas[1]}x1c, {moedas[2]}x2c, {moedas[5]}x5c, {moedas[10]}x10c, {moedas[20]}x20c, {moedas[50]}x50c, {moedas[100]}x1e, {moedas[200]}x2e ({troco}); Volte sempre!")

def main():
    cabinetel=cabine()

    estados={
        "LEVANTAR":cabinetel.levantar,
        "MOEDA":cabinetel.moeda,
        "ABORTAR":cabinetel.abortar,
        "T":cabinetel.telefonema,
        "POUSAR":cabinetel.pousar
    }

    while(True):
        linha=input()
        linha=linha.strip()

        acao = re.search(r"^\w*",linha.upper()).group()

        if acao in estados:
            estados[acao](linha)
        else:
            print("maq: Comando inválido")


if __name__ != "main":
    main()
