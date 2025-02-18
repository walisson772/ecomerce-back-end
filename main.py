from pathlib import Path
import json
import os

PRODUTOS = [
    {'id':0, 'produto':'Poco x7 pro', 'preco':3_000},
    {'id':1,'produto':'Iphone 14', 'preco':4_000},
    {'id':2,'produto':'Iphone 14 pro max', 'preco':5_000},
    {'id':3,'produto':'Poco x6 pro', 'preco':1_900},
]

ROOT_DIR = Path(__file__).parent
FILE_JSON = 'user.json'
FILE = ROOT_DIR / FILE_JSON

    

def listar_produtos(produtos):
    print()
    for produto in produtos:
        print(f'{produto['id']}) Item: {produto['produto']} Preço: {produto['preco']}')
    print()


def filtrar_valores(produtos, min, max):
    print()
    print(f'Itens entre os valores {min} e {max}')
    for produto in produtos:
        if produto['preco'] >= min and produto['preco'] <= max:
            print(f'{produto['id']}) Item: {produto['produto']} Preço: {produto['preco']}')
    print()

def itens_json(produtos, file):
    listar_produtos(produtos)
    response = int(input('Digite o numero referente ao seu desejo: '))
    carrinho = 0
    for produto in produtos:
        if response == produto['id']:
            carrinho += produto['preco']
            item = produto['produto']
    values = [{'valor':carrinho, 'produto':item}]
    with open(file, 'w', encoding='utf-8') as arquivo:
        json.dump(values, arquivo, ensure_ascii=False, indent=2)

def ver_carrinho(file):
    with open(file, 'r', encoding='utf-8') as arquivo:
        produto = json.load(arquivo)

    for dados in produto:
        produto = dados['produto']
        valor = dados['valor']

    print('<><><>' * 10)
    print(f'Atualmente você tem \033[34m{produto}\033[0m em seu carrinho')
    print(f'\033[34m{produto}\033[0m está custando \033[34m{valor}$\033[0m')    
    print('<><><>' * 10)

def opcoes():
    try:
        print('\033[32m1) Filtrar valores\033[0m')
        print('\033[32m2) Ver itens do carrinho\033[0m')
        print('\033[32m3) Adicionar item ao carrinho\033[0m')
        print('\033[32m4) Sair\033[0m')
    except ValueError:
        print('Digite apenas numeros')
    
    response = int(input('O que você deseja: '))
    return response

while True:
    try:
        response = opcoes()

        if response == 1:
            min = float(input('Digite o valor minimo: '))
            max = float(input('Digite o valor maximo: '))
            filtrar_valores(PRODUTOS, max=max, min=min)

        elif response == 2:
            ver_carrinho(FILE)

        elif response == 3:
            itens_json(PRODUTOS, FILE)

        else:
            os.system('cls')
            print('Essa opção não existe')
            continue
    except ValueError:
        os.system('cls')
        print('\033[31mDigite apenas numeros referentes ao numero do item desejado\033[0m')

    except FileNotFoundError:
        os.system('cls')
        print('\033[31mVocê não tem item nenhum no seu carrinho\033[0m')