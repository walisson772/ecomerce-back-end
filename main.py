PRODUTOS = [
    {'id':0, 'produto':'Poco x7 pro', 'preco':3_000},
    {'id':1,'produto':'Iphone 14', 'preco':4_000},
    {'id':2,'produto':'Iphone 14 pro max', 'preco':5_000},
    {'id':3,'produto':'Poco x6 pro', 'preco':1_900},
]

class Ecommerce:
    def __init__(self, produtos):
        self.produtos = produtos
        self.carrinho_item = 0

    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto['id']}) Item: {produto['produto']} Preço: {produto['preco']}')

    def filtrar_valores(self, min, max):
        for produto in self.produtos:
            if produto['preco'] >= min and produto['preco'] <= max:
                print(f'{produto['id']}) Item: {produto['produto']} Preço: {produto['preco']}')


def opcoes():
    print('1) Listar produtos')
    print('2) Filtrar valores')
    
    response = int(input('O que você deseja: '))
    return response

c = 0
while c < 3:
    response = opcoes
    ecommerce = Ecommerce(PRODUTOS)
    if response == 1:
        ecommerce.listar_produtos()

    elif response == 2:
        min = float(input('Digite o valor minimo: '))
        max = float(input('Digite o valor maximo: '))
        ecommerce.filtrar_valores(min, max)

    
# min = float(input('Digite o valor minimo: '))
# max = float(input('Digite o valor maximo: '))
# filtrar_valores(PRODUTOS,min, max)