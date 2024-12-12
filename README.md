# Sistema Distribuído com Comunicação Cliente-Servidor

## Introdução

Este sistema distribuído foi desenvolvido para fornecer um serviço de consulta a um catálogo de produtos utilizando Sockets e RPC/gRPC para a comunicação entre cliente e servidor. Ele permite buscar produtos, listar produtos abaixo de um preço específico e atualizar o estoque dos produtos.

## Execução do Sistema

Para executar o sistema, siga os passos abaixo:

1. Certifique-se de que o servidor esteja executando corretamente.
2. Execute `menu.py` para usar o gRPC ou `menuSocket.py` para usar Sockets.
3. Realize as operações desejadas (consultar produtos, atualizar estoque, etc.).
4. O servidor processará as solicitações e retornará as respostas ao cliente.

## Comparação entre Sockets e gRPC

### Sockets
**Vantagens:**
- Simplicidade na implementação e configuração.
- Comunicação direta entre cliente e servidor.

**Desvantagens:**
- Gestão manual de conexões e comunicação.
- Pode ser mais lento e menos escalável comparado ao gRPC.

### gRPC
**Vantagens:**
- Comunicação mais rápida e escalável.
- Gestão automática de conexões e comunicação.

**Desvantagens:**
- Configuração mais complexa, requer definição de arquivos `.proto`.
- Implementação e depuração mais difíceis.

## Diagrama de Fluxo de Comunicação

Aqui está um diagrama que ilustra o fluxo de comunicação entre cliente e servidor:

```mermaid
graph TD;
    A[Cliente] -->|Solicitação de Produto| B[Servidor];
    B -->|Resposta com Detalhes do Produto| A;
    A -->|Solicitação de Produtos Baratos| B;
    B -->|Resposta com Lista de Produtos| A;
    A -->|Solicitação de Atualização de Estoque| B;
    B -->|Resposta de Confirmação| A;
