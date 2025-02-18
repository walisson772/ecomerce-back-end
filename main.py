from pathlib import Path
import json

PRODUTOS = [
    {'id':0, 'produto':'Poco x7 pro', 'preco':3_000},
    {'id':1,'produto':'Iphone 14', 'preco':4_000},
    {'id':2,'produto':'Iphone 14 pro max', 'preco':5_000},
    {'id':3,'produto':'Poco x6 pro', 'preco':1_900},
]

ROOT_DIR = Path(__file__).parent
FILE_JSON = 'user.json'
FILE = ROOT_DIR / FILE_JSON

class Ecommerce:
    def __init__(self, produtos):
        self.produtos = produtos
        self.carrinho_item = 0
        self.app_json()
        

    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto['id']}) Item: {produto['produto']} Preço: {produto['preco']}')

    def filtrar_valores(self, min, max):
        for produto in self.produtos:
            if produto['preco'] >= min and produto['preco'] <= max:
                print(f'{produto['id']}) Item: {produto['produto']} Preço: {produto['preco']}')

    def app_json(self):
        self.values = [
                {
                   'valor':self.carrinho_item
            }   
        ]
        with open(FILE, 'w', encoding='utf-8') as arquivo:
            json.dump(self.values, arquivo, ensure_ascii=False, indent=2)

    def cadastrar(self):
        

def opcoes():
    print('1) Listar produtos')
    print('2) Filtrar valores')
    
    response = int(input('O que você deseja: '))
    return response

ecommerce = Ecommerce(PRODUTOS)
    
# min = float(input('Digite o valor minimo: '))
# max = float(input('Digite o valor maximo: '))
# filtrar_valores(PRODUTOS,min, max)