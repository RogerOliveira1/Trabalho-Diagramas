class jogador:
    def __init__(self):
        self.nome = None

    def preencher_nome(self, nome):
        self.nome = nome
    
    def obter_nivel(valor):
        if 0 <= valor < 50:
         return "Nível Baixo"
        elif 50 <= valor < 80:
          return "Nível Médio"
        elif 80 <= valor <= 100:
            return "Nível Alto"
    def atacar(self, alvo, valor_dano):
     print(f"{self.nome} atacou {alvo.nome} causando {valor_dano} pontos de dano.")
     alvo.receber_dano(valor_dano)
    def usar_item(self, item, alvo=None):
        if item in self.itens:
            print(f"{self.nome} usou o item: {item}")
            if alvo:
                alvo.receber_buff(item)
            self.itens.remove(item)
class Monstro:
    def __init__(self, tipo, poder, vida, ataque):
        self.tipo = tipo
        self.poder = poder
        self.vida = vida
        self.ataque = ataque

    def exibir_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Poder: {self.poder}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")

class MonstroOgro(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(tipo="Ogro", poder="Força Bruta", vida=vida, ataque=ataque)
        self.habilidade_especial = "Esmagar"


class MonstroMagoNegro(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(tipo="Mago Negro", poder="Magia Negra", vida=vida, ataque=ataque)
        self.habilidade_especial = "Explosão Mágica"
class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def utilizar(self, alvo=None):
        print(f"O item '{self.nome}' foi utilizado.")
        if alvo:
            print(f"Aplicando efeito do item em {alvo}.")
