class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade =35): #dander init
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod #decoretor, como se fosse ua função global
    def metodo_estatico():
        return 42
    
    @classmethod #é utilizado quando queremos acessar dados da propria classe
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'
if __name__ == "__main__":
    renzo = Pessoa(nome = 'Renzo')
    luciano = Pessoa(renzo,nome= 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' #cria um atributo
    del luciano.filhos #deleta um atributo
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__) #dict mostra os atributos de instancias de um ojeto
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(renzo.olhos)
    print( id(Pessoa.olhos), id(renzo.olhos), id(luciano.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.metodo_estatico())