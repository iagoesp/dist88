### Trabalho feito pelo aluno Iago Pinto, matrícula 201523035 ###
### do curso Ciências da Computação para a  disciplina MATA88 ###
### ministrado pelo professor Raimundo Macedo. Foi solicitada ###
### uma aplicação com arquitetura cliente-servidor.  O codigo ###
### foi implementado utilizando o framework 'QtDesigner' para ###
### definir  o layout,  a biblioteca  'PyQt5'  para converter ###
### os elementos do layout em codigo para executar no Python  ###
### e as bibliotecas 'Socket' e 'Thread' para definir e esta- ###
### belecer a comunicação  entre  o servidor e aplicação para ###
### cada cliente.                                             ###



import socket
from threading import Thread
from PyQt5 import QtGui, QtWidgets
import re
from objetos_do_layout import *
import sys
from functools import partial

## Define a classe de Exibição Inicial para inicializar a tela
## e algumas interações com botões
class Client(QtWidgets.QMainWindow, Ui_Program):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        ### Instancia um soquete para se comunicar com o servidor  ###
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ### Estabelece  a conexão com um endereço e uma porta específicos  para ###
        ### enviar solicitar requisições ao servidor com os parâmetros definido ###
        client.connect(('127.0.0.1', 9999))

        ### Salva a instância da conexão para o atual cliente ###
        self.client = client
        ### Cria o campo de RG e nome para salvar as credencias do cliente ###
        self.rg = ""
        self.nome = ""
        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        ###############################################
        ## Botões que acessam opções na tela Inicial ##
        ###############################################
        self.b_login.clicked.connect(self.goLoginScreen)
        self.b_cadastro.clicked.connect(self.goCadastroScreen)

        #############################################
        ## Botões que acessam opções na tela Login ##
        #############################################
        self.b_voltar_login.clicked.connect(partial(self.goInicio, self.w_login))
        self.b_limpar_login.clicked.connect(partial(self.goLimparLC, self.t_rg_login))
        self.b_entrar_login.clicked.connect(partial(self.goLogin, self.w_login, self.t_rg_login))

        ################################################
        ## Botões que acessam opções na tela Cadastro ##
        ################################################
        self.b_voltar_cadastro.clicked.connect(partial(self.goInicio, self.w_cadastro))
        self.b_limpar_cadastro.clicked.connect(partial(self.goLimparLC, self.t_rg_cadastro, self.t_nome_cadastro))
        self.b_entrar_cadastro.clicked.connect(partial(self.goCadastro, self.w_cadastro, self.t_rg_cadastro, self.t_nome_cadastro))

        #################################################
        ## Botões que acessam opções na tela Operacoes ##
        #################################################
        self.b_sacar.clicked.connect(self.goSacarScreen)
        self.b_depositar_2.clicked.connect(self.goDepositarScreen)
        self.b_transferir.clicked.connect(self.goTransferirScreen)
        self.b_sair.clicked.connect(self.goSair)
        
        #################################################
        ## Botões que acessam opções na tela Depositar ##
        #################################################
        self.b_voltar_2.clicked.connect(partial(self.goOperacoes, self.w_depositar))
        self.b_limpar_2.clicked.connect(partial(self.goLimparLC, self.t_rs))
        self.b_depositar.clicked.connect(partial(self.goDepositar, self.w_depositar, self.t_rs))

        ##################################################
        ## Botões que acessam opções na tela Transferir ##
        ##################################################
        self.b_voltar_4.clicked.connect(partial(self.goOperacoes, self.w_transferir))
        self.b_limpar_4.clicked.connect(partial(self.goLimparLC, self.t_rs_2, self.t_rg_2))
        self.b_transferir_2.clicked.connect(partial(self.goTransferir, self.w_cadastro, self.t_rg_2, self.t_rs_2))

        #############################################
        ## Botões que acessam opções na tela Sacar ##
        #############################################
        self.b_voltar_5.clicked.connect(partial(self.goOperacoes, self.w_sacar))
        self.b_limpar_5.clicked.connect(partial(self.goLimparLC, self.t_rs_3))
        self.b_sacar_2.clicked.connect(partial(self.goSacar, self.w_sacar, self.t_rs_3))

    ####################################################
    ## Acessando novas telas a partir da tela Inicial ##
    ####################################################
    ### Exibe a tela de Login ###
    def goLoginScreen(self):
        self.w_bemvindo.hide()
        self.w_login.show()

    ### Exibe a tela de Cadastro ###
    def goCadastroScreen(self):
        self.w_bemvindo.hide()
        self.w_cadastro.show()

    ######################################################
    ## Acessando novas telas a partir da tela Operações ##
    ######################################################
    ### Exibe a tela de Sacar ###
    def goSacarScreen(self):
        self.w_sacar.show()
        self.w_operacoes.hide()

    ### Exibe a tela de Deposito ###
    def goDepositarScreen(self):
        self.w_depositar.show()
        self.w_operacoes.hide()

    ### Exibe a tela de Transferência ###
    def goTransferirScreen(self):
        self.w_transferir.show()
        self.w_operacoes.hide()

    ##################
    ## Tela de Erro ##
    ##################
    ### Exibe a tela de erro, adicionando a mensagem de erro ###
    def goErroScreen(self, msg):
        self.w_erro.show()
        self.l_erro.setText(msg)
        self.b_ok_2.clicked.connect(self.byeErro)

    ### Fecha a tela de erro ###
    def byeErro(self):
        self.w_erro.hide()
        self.l_erro.setText("")
        

    ##############################################
    ## Funções que acessam opções da tela Login ##
    ##############################################
    def goInicio(self, tela_atual):
        tela_atual.hide()
        self.w_bemvindo.show()

    ### Limpa o campo de login ao clicar no botão "Limpar" ###
    def goLimparLC(self, rg, nome=None):
        rg.setText("")
        if(nome is not False):
            nome.setText("")

    #########################################
    ## Funções que checam o campo de texto ##
    #########################################
    #### Checa se há caracteres no campo ####
    def has_char(self, inputString):
        return bool(re.search(r'[a-zA-Z]', inputString))

    #### Checa se há números no campo ####
    def has_number(self, inputString):
        return bool(re.search(r'[0-9]', inputString))

    ################################################
    ###  Acessando   a    tela   de   Operações  ###
    ################################################
    ### Realiza o saque  obtendo o RG do próprio ###
    ### Configura a mensagem  inicial com o nome ###
    ### do cliente  e solicita o valor  do saldo ###
    ### que possui,  atualizando o valor na tela ###
    ################################################
    def goOperacoes(self, tela_atual):
        ##print("@@-- Operações --@@")
        tela_atual.hide()
        self.w_operacoes.show()
        self.l_operacoes.setText("O que você deseja, " + self.nome + "?")
        ##print("--id", self.rg)
        msg = "saldo#" + self.rg
        ##print("--msg", msg)
        self.send_msg(msg)
        msg = self.recv_msg()

        ##print("--msg", msg)
        msg = float(msg)
        ##print(msg)
        self.label.setText(self.label.text().split(":")[0] + ": R$" + str("{:.2f}".format(msg)))

    ################################################
    ### Acessando as telas a partir de Operações ###
    ################################################
    ### Realiza a transferência  obtendo o RG do ###
    ### destinatário e o valor  a ser depositado ### 
    ### e envia uma  mensagem para  o  servidor. ###
    ### Logo após, retorna para a tela Operações ###
    ################################################
    def goTransferir(self, tela_atual, rg, valor):
        ##print("@@-- Tranferir --@@")
        msg = "deposito#" + str(rg.text()) + "#" + str(valor.text()) + "#sacar#" + self.rg + "#" + str(valor.text())
        self.send_msg(msg)
        self.goOperacoes(self.w_transferir)
        
    ################################################
    ### Realiza o saque  obtendo o RG do próprio ###
    ### cliente e o valor a ser subtraído da sua ###
    ### conta e envia a mensagem para o servidor ###
    ### Logo após, retorna para a tela Operações ###
    ################################################
    def goSacar(self, tela_atual, valor):
        ##print("@@-- Sacar --@@")
        msg = "sacar#" + self.rg + "#" + str(valor.text())
        self.send_msg(msg)
        self.goOperacoes(self.w_sacar)
    
    ################################################
    ### Faz o  deposito obtendo o  RG do próprio ###
    ### cliente e o  valor a ser  somado na sua  ###
    ### conta e envia a mensagem para o servidor ###
    ### Logo após, retorna para a tela Operações ###
    ################################################
    def goDepositar(self, tela_atual, rs):
        ##print("@@-- Depositar --@@")
        if self.has_char(rs.text()):
            ##print("Erro deposito char")
            return
        msg = "deposito#" + str(self.rg) + "#" + str(rs.text())
        self.send_msg(msg)
        self.goOperacoes(self.w_depositar)

    ###################################################
    ### Checa se os campos de RG possuem algum erro ###
    ###################################################
    def goErrosRG(self, rg):
        if "#" in rg or "/" in rg:
            ##print("Erro # rg")
            return True

        ### Se o RG possui letras, retorna que é erro ###
        if self.has_char(rg):
            ##print("Erro rg char")
            return True    
        
        ### Se o tamanho do RG é zero, retorna que é erro ###
        if len(rg) == 0:
            ##print("Erro rg len")
            return True

    #####################################################
    ### Checa se os campos de nome possuem algum erro ###
    #####################################################
    def goErrosNome(self, nome):
        if "#" in nome or "/" in nome:
            ##print("Erro # nome")
            return True

        if self.has_number(nome):
            ##print("Erro nome number")
            return True      
        
        if len(nome) < 4:
            ##print("Erro nome len")
            return True

    #############################################
    ### Traduz os status de erro em mensagens ###
    #############################################
    def goErros(self, msg):
        if msg == "401":
            ##print("Erro 401")
            return True
        elif msg == "400":
            ##print("Erro 400")
            return True

    #############################################
    ### Valida os campos de login, se correto ###
    #############################################
    def goLogin(self, tela_atual, rg_text):
        ##print("@@-- Entrar --@@")
        rg = rg_text.text()
        
        ### Checa  se há algum erro na  entrada de RG ###
        ### como se possui letra ou tamanho incorreto ###
        if(self.goErrosRG(rg)):
            return
        
        ### Inicializa a conexão com o servidor ###
        self.begin_thread()

        ### Envia o RG para o servidor e checar se o id existe ###
        self.send_msg(rg_text.text())

        ### Recebe a resposta do servidor em relação ao RG enviado ###
        msg = self.recv_msg()
    
        ### Checa se há erros com o login, seja ###
        ### usuário inválido  ou não cadastrado ###
        if self.goErros(msg):
            return

        ### Salva o RG e o nome do cliente ###
        id = msg.split("#")
        self.rg = id[1].split("/")[0]
        self.nome = id[1].split("/")[1]
        
        ##print("--id", (self.rg, self.nome))
        ##print("Entrou")

        ### Vai para a tela de operações ###
        self.goOperacoes(tela_atual)

    ############################################
    ### Realiza o cadastro de novos usuários ###
    ############################################
    def goCadastro(self, tela_atual, rg_text, nome_text):
        ##print("@@-- Cadastro --@@")
        rg = rg_text.text()
        nome = nome_text.text()

        ### Checa  se há algum erro na  entrada de RG ###
        ### como se possui letra ou tamanho incorreto ###
        if(self.goErrosRG(rg)):
            return

        ### Checa  se há algum erro na  entrada de nome ###
        ### como se possui número  ou tamanho incorreto ###
        if(self.goErrosNome(nome)):
            return

        ### Inicializa a conexão com o servidor ###
        self.begin_thread()

        ### Envia o RG para o servidor e checar se o id existe ###
        self.send_msg(rg + "#" + nome)
  
        ### Recebe a resposta do servidor em relação ao RG enviado ###
        msg = self.recv_msg()
        ##print(msg)

        ### Checa se há erros com o login, seja ###
        ### usuário inválido  ou não cadastrado ###
        if self.goErros(msg):
            return

        ### Salva o RG e o nome do cliente ###
        id = msg.split("#")
        self.rg = id[1].split("/")[0]
        self.nome = id[1].split("/")[1]
        ##print("--id", (self.rg, self.nome))
        ##print("Entrou")
        self.goOperacoes(tela_atual)

    ### Encerra a aplicação respectiva do cliente ###
    #### e encerra a conexão com o servidor ###
    def goSair(self):
        self.send_msg("QUIT")
        QtWidgets.QApplication.quit()

    #############################################################
    ### Instancia threads para as funções de receber e enviar ###
    ### mensagem e rodar ambas paralelamente com a aplicação, ###
    ### sem comprometer a aplicação geral de cliente-servidor ###
    #############################################################
    def begin_thread(self):
        Thread(target=self.send_msg).start()
        Thread(target=self.recv_msg).start()

    ### Função responsável por enviar a mensagem para o servidor ###
    def send_msg(self, msg=""):
        ##print(msg)
        self.client.send(msg.encode())
        if (msg.upper() == "QUIT"):
            self.client.close()

    ### Função responsável por receber a mensagem enviada do servidor ###
    def recv_msg(self):
        while 1:
            try:
                data = self.client.recv(1024).decode()
                return data
            except:
                exit()

    ### Encerra a aplicação respectiva do cliente ###
    #### e encerra a conexão com o servidor ###
    def closeEvent(self, QCloseEvent):
        self.send_msg("QUIT")
        self.client.close()
        QtWidgets.QApplication.quit()

app = QtWidgets.QApplication(sys.argv)
main = Client()
main.show()
app.exec_()