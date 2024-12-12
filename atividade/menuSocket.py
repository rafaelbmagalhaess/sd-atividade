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
    subprocess.Popen(["python", "atividade/server/serverSocket.py"])   
    print("ESPERANDO RESPOSTA DO SERVIDOR")
    time.sleep(3)

def buscarProduto(s):
    limparTerminal()
    nome_produto = input("================================= DIGITE O NOME DO PRODUTO DESEJADO: ")
    s.sendall(json.dumps({"action": "buscarProduto", "nome": nome_produto}).encode())
    data = s.recv(1024)
    response = json.loads(data.decode())
    if "error" in response:
        print(response["error"])
    else:
        print(f"PRODUTO ENCONTRADO: {response['nome']}\nPREÇO: {response['preco']}\nESTOQUE: {response['estoque']}")

def procurarProdutoBarato(s):
    limparTerminal()
    preco_maximo = float(input("================================= DIGITE O PREÇO MÁXIMO: "))
    s.sendall(json.dumps({"action": "listarProdutosBaratos", "preco_maximo": preco_maximo}).encode())
    data = s.recv(1024)
    response = json.loads(data.decode())
    if response:
        print("FOI ENCONTRADO OS SEGUINTES PRODUTOS:")
        for produto in response:
            print(f"{produto['nome']} --- PREÇO: {produto['preco']} --- ESTOQUE: {produto['estoque']}")
    else:
        print("NÃO ENCONTRAMOS NADA ABAIXO DO PREÇO SOLICITADO!")

def atualizarProduto(s):
    limparTerminal()
    nome_produto = input("================================= DIGITE O PRODUTO PARA ATUALIZAR: ")
    novo_estoque = int(input("DIGITE A QUANTIDADE DO PRODUTO: "))
    s.sendall(json.dumps({"action": "atualizarEstoque", "nome": nome_produto, "novo_estoque": novo_estoque}).encode())
    data = s.recv(1024)
    response = json.loads(data.decode())
    if "error" in response:
        print(response["error"])
    else:
        print(response["mensagem"])

def menu():
    aguardando()
    limparTerminal()
    print("============= SERVIÇO DE ACESSO AO SERVIDOR =============")
    print("1                             Consultar produto pelo nome")
    print("2                   Consultar produtos abaixo de um preço")
    print("3                         Atualizar estoque de um produto")
    print("4                                                    Sair")
    print("=========================================================")

def run():
    if not verificaConexao():
        iniciaServidor()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 50051))

        while True:
            menu()
            choice = input("\n Digite o número da opção: ")
            if choice == '1':
                buscarProduto(s)
            elif choice == '2':
                procurarProdutoBarato(s)
            elif choice == '3':
                atualizarProduto(s)
            elif choice == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

def verificaConexao():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(('localhost', 50051))
        server.close()
        return True  
    except socket.error:
        return False 

if __name__ == "__main__":
    run()
