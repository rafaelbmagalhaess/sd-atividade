# Sistema Distribuído com Comunicação Cliente-Servidor

## Introdução

Este sistema distribuído foi desenvolvido para atender aos requisitos de um serviço de consulta a um catálogo de produtos distribuído. O sistema utiliza Sockets e RPC/gRPC para estabelecer a comunicação entre cliente e servidor.

## Execução do Sistema

Para executar o sistema, siga os passos abaixo:

1. Certifique-se de que o servidor esteja executando e configurado corretamente.
2. Execute menu.py (ele ira fazer a conexão do servidor).
3. Realize as operações desejadas (consultar produtos, atualizar estoque, etc.).
4. O servidor processará as solicitações e retornará as respostas ao cliente.

## Comparação entre Sockets e gRPC

Aqui está uma comparação entre as duas abordagens utilizadas no sistema:

### Sockets:
- **Vantagens:**
  - Fácil de implementar e configurar.
  - Permite uma comunicação direta entre cliente e servidor.
- **Desvantagens:**
  - Requer uma gestão manual de conexões e comunicação.
  - Pode ser mais lento e menos escalável do que o gRPC.

### gRPC:
- **Vantagens:**
  - Permite uma comunicação mais rápida e escalável.
  - Fornece uma gestão automática de conexões e comunicação.
- **Desvantagens:**
  - Requer uma configuração mais complexa e a definição de um arquivo `.proto`.
  - Pode ser mais difícil de implementar e depurar.

## Diagrama de Fluxo de Comunicação

Aqui está um diagrama simples que ilustra o fluxo de comunicação entre cliente e servidor:

## Código-Fonte do Sistema

O código-fonte do sistema está disponível nos arquivos do repositório.

