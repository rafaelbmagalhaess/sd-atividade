import socket
import threading
import json

class CatalogServiceServicer:
    def __init__(self):
        self.catalogo = {
            "Computador": {"nome": "Computador", "preco": 1000.0, "estoque": 10},
            "Caneta": {"nome": "Caneta", "preco": 20.0, "estoque": 50}
        }

    def buscarProduto(self, nome):
        print(f"PROCURANDO POR: {nome}")
        produto = self.catalogo.get(nome)
        if produto:
            return json.dumps(produto)
        else:
            return json.dumps({"error": "NÃO ENCONTRADO - TENTE NOVAMENTE"})

    def listarProdutosBaratos(self, preco_maximo):
        print(f"PROCURANDO POR PRODUTOS ABAIXO DE: {preco_maximo}")
        produtos = [p for p in self.catalogo.values() if p["preco"] < preco_maximo]
        return json.dumps(produtos)

    def atualizarEstoque(self, nome, novo_estoque):
        print(f"ATUALIZANDO {nome} PARA QUANTIDADE {novo_estoque}")
        if nome in self.catalogo:
            self.catalogo[nome]["estoque"] = novo_estoque
            return json.dumps({"mensagem": "PRODUTO ATUALIZADO COM SUCESSO"})
        else:
            return json.dumps({"error": "NÃO ENCONTRADO - TENTE NOVAMENTE"})

    def handle_client(self, conn, addr):
        print(f"Conectado a {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                request = json.loads(data.decode('utf-8'))
                action = request.get("action")
                if action == "buscarProduto":
                    response = self.buscarProduto(request.get("nome"))
                elif action == "listarProdutosBaratos":
                    response = self.listarProdutosBaratos(request.get("preco_maximo"))
                elif action == "atualizarEstoque":
                    response = self.atualizarEstoque(request.get("nome"), request.get("novo_estoque"))
                conn.sendall(response.encode('utf-8'))

def serve():
    catalog_service = CatalogServiceServicer()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 50051))
        s.listen()
        print("============ SERVIDOR INICIADO COM SUCESSO ==============")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=catalog_service.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    serve()
