import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import grpc
import catalog_pb2
import catalog_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = catalog_pb2_grpc.ServicoCatalogoStub(channel)

    
    response = stub.buscarProduto(catalog_pb2.RequisicaoProduto(nome="Computador"))
    print(f"Produto: {response.produto}")

    
    response = stub.listarProdutosBaratos(catalog_pb2.RequisicaoPreco(preco_maximo=500.0))
    print("Produtos abaixo do preço:")
    for produto in response.produtos:
        print(produto)

   
    response = stub.atualizarEstoque(catalog_pb2.RequisicaoAtualizarEstoque(nome="Computador", novo_estoque=5))
    print(response.mensagem)

if __name__ == "__main__":
    run()
