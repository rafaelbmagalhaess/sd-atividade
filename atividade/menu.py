import grpc
import catalog_pb2
import catalog_pb2_grpc
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
    limparTerminal() 
    time.sleep(3)  

def buscarProduto(stub):
    limparTerminal()
    nome_produto = input("================================= DIGITE O NOME DO PRODUTO DESEJADO:")
    try:
        response = stub.buscarProduto(catalog_pb2.RequisicaoProduto(nome=nome_produto))
        if response.produto:
            print(f"PRODUTO ENCONTRADO: {response.produto.nome}\nPREÇO: {response.produto.preco}\nESTOQUE: {response.produto.estoque}")
        else:
            print("NÃO FOI ENCONTRADO O PRODUTO DESEJADO!")
    except grpc.RpcError as e:
        print(f"Tivemos problemas ao procurar o produto: {e.details()}")

def procurarProdutoBarato(stub):
    limparTerminal()
    preco_maximo = float(input("================================= DIGITE O PREÇO MÁXIMO: "))
    try:
        response = stub.listarProdutosBaratos(catalog_pb2.RequisicaoPreco(preco_maximo=preco_maximo))
        if response.produtos:
            print("FOI ENCONTRADO OS SEGUINTES PRODUTOS:")
            for produto in response.produtos:
                print(f"{produto.nome} --- PREÇO: {produto.preco} --- ESTOQUE: {produto.estoque}")
        else:
            print("NÃO ENCONTRAMOS NADA ABAIXO DO PREÇO SOLICITADO!")
    except grpc.RpcError as e:
        print(f"ERRO AO REALIZAR CONSULTA: {e.details()}")

def atualizarProduto(stub):
    limparTerminal()
    nome_produto = input("================================= DIGITE O PRODUTO PARA ATUALIZAR: ")
    novo_estoque = int(input("DIGITE A QUANTIDADE DO PRODUTO:"))
    try:
        response = stub.atualizarEstoque(catalog_pb2.RequisicaoAtualizarEstoque(nome=nome_produto, novo_estoque=novo_estoque))
        print(response.mensagem)
    except grpc.RpcError as e:
        print(f"ERRO AO ATUALIZAR O PRODUTO: {e.details()}")

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

    channel = grpc.insecure_channel("localhost:50051")
    stub = catalog_pb2_grpc.ServicoCatalogoStub(channel)

    while True:
        menu()
        choice = input("\n Digite o número da opção: ")
        if choice == '1':
            buscarProduto(stub)
        elif choice == '2':
            procurarProdutoBarato(stub)
        elif choice == '3':
            atualizarProduto(stub)
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def verificaConexao():
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(('localhost', 50051))
        server.close()
        return True  
    except socket.error:
        return False 

if __name__ == "__main__":
    run()
