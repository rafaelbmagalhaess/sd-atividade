import socket
import json
import subprocess
import time
import os

def aguardando():
    input("\nPressione Enter para continuar...")

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciaServidor():
    print("============ SOLICITANDO SERVIDOR ============")
    time.sleep(2)
    limparTerminal()
    subprocess.Popen(["python", "atividade/server/server.py"])   
    print("ESPERANDO RESPOSTA DO SERVIDOR")
    time.sleep(3)

def buscarProduto(s):
    limparTerminal()
    nome_produto = input("================================= DIGITE O NOME DO PRODUTO DESEJADO: ")
    s.sendall(json.dumps({"action": "buscarProduto", "nome": nome_produto}).encode('utf-8'))
    data = s.recv(1024)
    response = json.loads(data.decode('utf-8'))
    if "error" in response:
        print(response["error"])
    else:
        print(f"PRODUTO ENCONTRADO: {response['nome']}\nPREÇO: {response['preco']}\nESTOQUE: {response['estoque']}")

def procurarProdutoBarato(s):
    limparTerminal()
    preco_maximo = float(input("================================= DIGITE O PREÇO MÁXIMO: "))
    s.sendall(json.dumps({"action": "listarProdutosBaratos", "preco_maximo": preco_maximo}).encode('utf-8'))
    data = s.recv(1024)
    response = json.loads(data.decode('utf-8'))
    if response:
        print("FOI ENCONTRADO OS SEGUINTES PRODUTOS:")
        for produto in response:
            print(f"{produto['nome']} --- PREÇO: {produto['preco']} --- ESTOQUE: {produto['estoque']}")
    else:
        print("NÃO ENCONTRAMOS NADA ABAIXO DO PREÇO SOLICITADO!")

def atualizarProduto(s):
    limparTerminal