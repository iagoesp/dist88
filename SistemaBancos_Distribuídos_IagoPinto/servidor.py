import socket
from threading import Thread

class Server:
    def __init__(self):
        ### Instancia um soquete para se comunicar com os clientes ###
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ### Esse método  conecta  o  servidor  para que receba ###
        ### requisições em um endereço e uma porta específicos ###
        server.bind(('127.0.0.1', 9999))

        ### Configura o soquete para ficar no modo de escuta, aguardando conexões ### 
        server.listen(5)

        ### Salva a conexão do servidor ###
        self.server = server

        ### Cria uma lista de objetos de clientes ###
        self.li = []  
        self.clients = {}

        ### Método para obter todas as conexões requisitidas ###
        self.get_con()

    ### Aguarda todas as conexões requisitadas por clientes, para estabelecer uma conexão ###
    def get_con(self):
        print("get connection")

        while 1:
            ### Estabele a conexão com o cliente ###
            con, addr = self.server.accept()
            ### Responde ao método begin_thread() do cliente ###
            ### É  somente  para  dar um ping / uma resposta ###
            data = ""
            con.send(data.encode())
            ### Inicia uma thread para habilitar a troca ###
            ### de mensagens com  cada cliente conectado ###
            Thread(target=self.get_msg, args=(con, self.li, addr)).start()

            ### Adiciona a conexão em uma lista de conexões ###
            self.li.append(con)

    ### Método para realizar a troca de mensagens ###
    ### com o cliente/conexão respectiva ###
    def get_msg(self, con, li, addr):
        print("get msg")

        ### Laço para receber as credenciais do cliente e checar se é cadastro ou login ###
        while 1:
            ### Recebe a mensagem com as credenciais do cliente ###
            name = con.recv(1024).decode()
            ### Se há um caractere '#',  é porque a operação é  'Cadastro' ###
            ### E foi passado o id e o nome do atual cliente como mensagem ###
            if '#' in name:

                ### Contudo,  se o  id do  cliente já  estiver  na  lista de  clientes, ###
                ### o cadastro é negado, pois já possui um outro usuário com o mesmo id ###
                ### e retornará  uma mensagem de erro com status  '400'  para o cliente ###
                ### Caso contrário,  o usuário terá suas credenciais salvas no servidor ###
                ### e será enviado uma resposta com status '200' com os ids respectivos ###
                id = name.split("#")
                
                if id[0] in self.clients:
                    msg = "400"
                    ##print(msg)
                    con.send(msg.encode())
                else:
                    self.clients[id[0]] = {}
                    self.clients[id[0]]["rg"] = id[0]
                    self.clients[id[0]]["nome"] = id[1]
                    self.clients[id[0]]["saldo"] = 0
                    self.clients[id[0]]["conn"] = con
                    msg = "200#" + id[0] + "/" + id[1]
                    con.send(msg.encode())
                    break

            ### Se não houver o caractere '#', então a operação a ser realizada é o login ###
            ### Se o  cliente já esteja  previamente cadastrado,  ele loga no sistema e é ###
            ### enviado  uma mensagem com  o status  '200'  e as credenciais  respectivas ###
            ### Se não, somente é enviado  uma mensagem com o status '401" para o cliente ###

            else:
                if name in self.clients:
                    msg = "200#" + name + "/" + self.clients[name]["nome"]
                    con.send(msg.encode())
                    break
                else:
                    msg = "401"
                    con.send(msg.encode())

        ### Realiza um  recebimento  e envio de  mensagens cíclicas, indefinidamente  até que ###
        ### a conexão seja  encerrada.  Então, a cada mensagem  enviada pelo cliente,  haverá ###
        ### uma resposta enviada do servidor dependendo de cada mensagem enviada pelo cliente ###
        while 1:
            redata = ""
            ##print("ok")
            try:
                ### Recebe  as requisições  enviadas  pelo cliente  através ###
                ### de uma  mensagem.  Com um parser  aplicado,  é obtido a ###
                ### operação, o id do cliente e um valor numeral, se houver ###
                print("waiting answer")
                redata = con.recv(1024).decode()
                ### id[0] é a operação
                ### id[1] é o id do cliente 
                ### id[2] é o valor que foi pasasdo em R$, se houver 
                
                ### Há três operações  a serem realizadas:  a de checar o saldo. ###
                ### de realizar  um depósito  ou uma  transferência.  A operação ###
                ### de depósito é feita para a conta do próprio cliente, com uma ###
                ### operação  de somar o  valor recebido  e obter um novo saldo. ###
                ### A operação  de sacar é uma operação  de subtração  do  valor ###
                ### do cliente com o valor que foi inserido,  retornando um novo ###
                ### valor.  A operação de saldo  envia o saldo atual  ao cliente ###

                ### A operação  de  transferência  envia para  o  servidor uma string ###
                ### contendo duas operações a serem realizadas:  de  depósito  para o ### 
                #### destinatário somando o valor que  foi inserido com o saldo atual ###
                ### com o valor inserido,  e de saque,  que subtrai o  saldo atual do ###
                ### que enviou o valor para o destinatário ### 
                ##print(redata)
                if "#" in redata:
                    msg = redata.split("#")
                    if msg[0] == "saldo":
                        ##print(msg[0], msg[1])
                        msg = str(self.clients[msg[1]]["saldo"])
                        con.send(msg.encode())
                    if msg[0] == "deposito":
                        ##print(msg[0], msg[1], msg[2])
                        self.clients[msg[1]]["saldo"] += float(msg[2])
                        if len(msg) > 3:
                            msg = msg[3:6]
                    if msg[0] == "sacar":
                        ##print(msg[0], msg[1], msg[2])
                        self.clients[msg[1]]["saldo"] -= float(msg[2])

            ### Se ocorrer algum erro durante as operações ###
            ### o servidor encerra a conexão com o cliente ###
            except Exception as e:
                print(e)
                for c in self.clients:
                    if con == self.clients[c]["conn"]:
                        self.clients[c]["conn"] = False
                        break
                self.close_client(con, addr)
                break
            
            ### Se o cliente encerrar  a  aplicação,  é enviado um comando ###
            ### para que o servidor possa encerrar a conexão com o cliente ###
            if (redata.upper() == "QUIT"):
                for c in self.clients:
                    if con == self.clients[c]["conn"]:
                        self.clients[c]["conn"] = False
                        break
                self.close_client(con, addr)
                break

    ### Encerra a conexão com o cliente ###
    def close_client(self, con, addr):
        print("close_client")
        self.li.remove(con)
        con.close()

if __name__ == "__main__":
    Server()