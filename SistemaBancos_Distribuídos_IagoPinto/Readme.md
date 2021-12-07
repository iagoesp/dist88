# Projeto de Implementação: Sistema Distribuído Simples para Manutenção de Contas Bancárias

Trabalho feito pelo aluno Iago Pinto, matrícula 201523035 do curso Ciências da Computação para a  disciplina MATA88 ministrado pelo professor Raimundo Macedo.

Foi solicitada uma aplicação com arquitetura cliente-servidor para um problema de um sistema de bancos com o uso de servidor e clientes. 

O código foi implementado utilizando o framework 'QtDesigner' para desenhar e definir o layout, a biblioteca  'PyQt5'  para converter os elementos do layout em código para importar para o código no Python e as bibliotecas 'Socket' e 'Thread' para definir e estabelecer a comunicação  entre  o servidor e aplicação para cada cliente.


## Instalação

A versão do Python que foi utilizado na implementação do trabalho é [3.9.9](https://www.python.org/dev/peps/pep-0596/).

Para instalar os pacotes abaixo, é necessário utilizar o [pip](https://pip.pypa.io/en/stable/).

Como citado acima, foi utilizado três bibliotecas. Contudo, o [socket](https://docs.python.org/pt-br/3/library/socket.html?highlight=socket#module-socket) e o [threading](https://docs.python.org/pt-br/3/library/threading.html?highlight=threading#module-threading) são módulos nativos do Python.

A biblioteca PyQt5 não é nativo do Python 3.9.9 e é necessário a instalação.
Para isso, foi utilizado o comando para obter a biblioteca.
```bash
python3 -m pip install PyQt5
```

## Código

O código dos trabalhos estão comentados e disponíveis nos links abaixo.

[Arquivo do Cliente]() - link para o arquivo no github

[Arquivo do Servidor]() - link para o arquivo no github

```python
# Para o layout, do lado do cliente
import PyQt5

# Para a manutenção do servidor
import socket
from threading import Thread
```
## 

## Demonstração de Uso - Vídeo

[Vídeo](https://youtu.be/4fHmGWs34fA)

## Exemplo de Uso
 O executável encontra-se no repositório do Drive, pois excedeu o tamanho limite que o GitHub oferece.
 
 [Repositório](https://drive.google.com/drive/folders/1RzVxpLVHXKvbypghMwQe6spke6gYBz9H?usp=sharing): https://drive.google.com/drive/folders/1RzVxpLVHXKvbypghMwQe6spke6gYBz9H?usp=sharing
 
 O exemplo de uso com as imagens encontra-se no pdf.
 
 [PDF](https://github.com/iagoesp/dist88/blob/main/DOCUMENTAC%CC%A7A%CC%83O%20DA%20APLICAC%CC%A7A%CC%83O_%20%E2%80%9CSISTEMA%20DE%20BANCOS%E2%80%9D.pdf)
### Passo 1 - Executando 

1. Inicialmente, roda o arquivo do servidor:
- Executável/servidor.exe

  - Caso não esteja funcionando o executável acima, pode rodar o arquivo em python servidor.py

2. Logo após, roda o arquivo do cliente:
- Executável/servidor.exe

  - Caso não esteja funcionando o executável acima, pode rodar o arquivo em python cliente.py

3. Aparece a tela inicial. Há dois botões: um de Login e o outro de Cadastro.

4. Como não há nenhum cliente ativo, é necessário clicar no botão "Cadastro".

5. Na tela de Cadastro, há dois campos: nome e RG. Há também três botões, um de "Voltar", um de "Limpar" e outro de "Entrar"
    - no botão de "Voltar", volta para a tela inicial
    - no botão de "Limpar", limpa todos os campos
    - no botão de "Voltar", verifica se há o mesmo ID cadastrado. Se não houver, salva e cadastra as instâncias do cliente e direciona para a tela de Operações.

6. Na tela de Operações, há uma mensagem com o nome do cliente, recebido diretamente do servidor. Há também três opções: Sacar, Depositar e Transferir. Sacar subtrai do saldo atual do cliente; Depositar adiciona o valor para o saldo atual e Transferir deposita o valor na conta de outro cliente. Todos as as operações são realizadas diretamente no servidor.

7. Para sacar, há um campo de dinheiro, em reais, para substrair o valor atual. Há três botões, um de "Voltar", um de "Limpar" e outro de "Sacar"
    - no botão de "Voltar", volta para a tela de Operações
    - no botão de "Limpar", limpa todos os campos
    - no botão de "Voltar", efetua a operação de saque. Essa operação é realizada no servidor. Logo após, direciona para a tela de Operações.

8. Para depositar, há um campo de dinheiro, em reais, para adicionar ao valor atual. Há três botões, um de "Voltar", um de "Limpar" e outro de "Depositar"
    - no botão de "Voltar", volta para a tela de Operações
    - no botão de "Limpar", limpa todos os campos
    - no botão de "Depositar", efetua a operação de depósito. Essa operação é realizada no servidor. Logo após, direciona para a tela de Operações.

9. Para transferir, há um campo de dinheiro, em reais, para depositar o valor na conta do destinatário. Há outro campo contendo o RG do destinatário. Também há três botões, um de "Voltar", um de "Limpar" e outro de "Transferir"
    - no botão de "Voltar", volta para a tela de Operações
    - no botão de "Limpar", limpa todos os campos
    - no botão de "Transferir", efetua a operação de transferência. Essa operação é realizada se houver um RG válido no servidor e também é efetuada lá. Logo após, direciona para a tela de Operações.

10. Por último, há o botão de "Sair" que encerra a conexão do cliente atual com o servidor.# distribuidos88
