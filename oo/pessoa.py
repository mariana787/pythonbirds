class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome = None, idade=40):
        self.nome = nome
        self.idade = idade
        self.filhos= list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 66

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro')
    luciano = Pessoa(pedro, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome='Damarco'
    pedro.sobrenome='Lazarento'
    del luciano.filhos
    luciano.olhos=1
    del luciano.olhos
    print(luciano.__dict__)
    print(pedro.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(pedro.olhos)
    print(id(pedro.olhos), id(luciano.olhos), id(Pessoa.olhos))
    print(pedro.metodo_estatico(), luciano.metodo_estatico(), Pessoa.metodo_estatico())
    print(pedro.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe(), Pessoa.nome_e_atributos_de_classe())