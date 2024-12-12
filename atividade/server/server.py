from concurrent import futures

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import grpc
import catalog_pb2
import catalog_pb2_grpc

class CatalogServiceServicer(catalog_pb2_grpc.ServicoCatalogoServicer):
    def __init__(self):
        self.catalogo = {
            "Computador": catalog_pb2.Produto(nome="Computador", preco=1000.0, estoque=10),
            "Caneta": catalog_pb2.Produto(nome="Caneta", preco=20.0, estoque=50)
        }

    def buscarProduto(self, request, context):
        print(f"PROCURANDO POR: {request.nome}")
        produto = self.catalogo.get(request.nome)
        if produto:
            return catalog_pb2.RespostaProduto(produto=produto)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("NÃO ENCONTRADO - TENTE NOVAMENTE")
            return catalog_pb2.RespostaProduto()

    def listarProdutosBaratos(self, request, context):
        print(f"PROCURANDO POR PRODUTOS ABAIXO DE: {request.preco_maximo}")
        produtos = [p for p in self.catalogo.values() if p.preco < request.preco_maximo]
        return catalog_pb2.RespostaProdutos(produtos=produtos)

    def atualizarEstoque(self, request, context):
        print(f"ATUALIZANDO {request.nome} PARA QUANTIDADE {request.novo_estoque}")
        if request.nome in self.catalogo:
            self.catalogo[request.nome].estoque = request.novo_estoque
            return catalog_pb2.RespostaAtualizarEstoque(mensagem="PRODUTO ATUALIZADO COM SUCESSO")
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("NÃO ENCONTRADO - TENTE NOVAMENTE")
            return catalog_pb2.RespostaAtualizarEstoque(mensagem="NÃO ENCONTRADO - TENTE NOVAMENTE")

def serve():
    print("============== SERVIDOR PROCESSANDO =====================")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    catalog_pb2_grpc.add_ServicoCatalogoServicer_to_server(CatalogServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("< << <<< SERVIDOR SENDO INICIADO NA PORTA 50051 >>> >> >")
    server.start()
    print("============ SERVIDOR INICIADO COM SUCESSO ==============")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
