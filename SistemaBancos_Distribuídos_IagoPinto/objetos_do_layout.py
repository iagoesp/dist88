# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bemvindo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

### Interface do programa definido nesse arquivo, ###
### com janelas, labels, frames e botões definidos ###

### O layout foi feito com o auxílio do programa QtDesigner, ###
### e, com o código em XML pronto, foi utilizado uma extensão ###
### para converter para elemento da biblioteca PyQt5 ###
class Ui_Program(object):
    ### Essa função instancia todos os elementos gráficos da aplicação ###
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 449)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## Elementos da interface inicial
        self.w_bemvindo = QtWidgets.QWidget(self.centralwidget)
        self.w_bemvindo.setGeometry(QtCore.QRect(80, 110, 231, 171))
        self.w_bemvindo.setObjectName("w_bemvindo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.w_bemvindo)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_login = QtWidgets.QPushButton(self.w_bemvindo)
        self.b_login.setObjectName("b_login")
        self.verticalLayout.addWidget(self.b_login)
        self.b_cadastro = QtWidgets.QPushButton(self.w_bemvindo)
        self.b_cadastro.setObjectName("b_cadastro")
        self.verticalLayout.addWidget(self.b_cadastro)

        ## Elementos da interface de Login
        self.w_login = QtWidgets.QWidget(self.centralwidget)
        self.w_login.setGeometry(QtCore.QRect(30, 70, 341, 261))
        self.w_login.setObjectName("w_login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.w_login)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.l_rg = QtWidgets.QLabel(self.w_login)
        self.l_rg.setObjectName("l_rg")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_rg)
        self.t_rg_login = QtWidgets.QLineEdit(self.w_login)
        self.t_rg_login.setObjectName("t_rg_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_rg_login)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 50, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.b_entrar_login = QtWidgets.QPushButton(self.w_login)
        self.b_entrar_login.setObjectName("b_entrar_login")
        self.gridLayout.addWidget(self.b_entrar_login, 0, 5, 1, 1)
        self.b_limpar_login = QtWidgets.QPushButton(self.w_login)
        self.b_limpar_login.setObjectName("b_limpar_login")
        self.gridLayout.addWidget(self.b_limpar_login, 0, 3, 1, 1)
        self.b_voltar_login = QtWidgets.QPushButton(self.w_login)
        self.b_voltar_login.setObjectName("b_voltar_login")
        self.gridLayout.addWidget(self.b_voltar_login, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        ## Elementos da interface de Cadastro
        self.w_cadastro = QtWidgets.QWidget(self.centralwidget)
        self.w_cadastro.setGeometry(QtCore.QRect(30, 80, 341, 250))
        self.w_cadastro.setObjectName("w_cadastro")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.w_cadastro)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.l_rg_3 = QtWidgets.QLabel(self.w_cadastro)
        self.l_rg_3.setObjectName("l_rg_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_rg_3)
        self.t_rg_cadastro = QtWidgets.QLineEdit(self.w_cadastro)
        self.t_rg_cadastro.setObjectName("t_rg_cadastro")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_rg_cadastro)
        self.l_nome_2 = QtWidgets.QLabel(self.w_cadastro)
        self.l_nome_2.setObjectName("l_nome_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l_nome_2)
        self.t_nome_cadastro = QtWidgets.QLineEdit(self.w_cadastro)
        self.t_nome_cadastro.setObjectName("t_nome_cadastro")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.t_nome_cadastro)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 50, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.b_entrar_cadastro = QtWidgets.QPushButton(self.w_cadastro)
        self.b_entrar_cadastro.setObjectName("b_entrar_cadastro")
        self.gridLayout_3.addWidget(self.b_entrar_cadastro, 0, 5, 1, 1)
        self.b_limpar_cadastro = QtWidgets.QPushButton(self.w_cadastro)
        self.b_limpar_cadastro.setObjectName("b_limpar_cadastro")
        self.gridLayout_3.addWidget(self.b_limpar_cadastro, 0, 3, 1, 1)
        self.b_voltar_cadastro = QtWidgets.QPushButton(self.w_cadastro)
        self.b_voltar_cadastro.setObjectName("b_voltar_cadastro")
        self.gridLayout_3.addWidget(self.b_voltar_cadastro, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.w_depositar = QtWidgets.QWidget(self.centralwidget)
        self.w_depositar.setGeometry(QtCore.QRect(30, 80, 341, 251))
        self.w_depositar.setObjectName("w_depositar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.w_depositar)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_deposito = QtWidgets.QLabel(self.w_depositar)
        self.l_deposito.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.l_deposito.setObjectName("l_deposito")
        self.verticalLayout_4.addWidget(self.l_deposito)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_4.setObjectName("formLayout_4")
        self.l_rs = QtWidgets.QLabel(self.w_depositar)
        self.l_rs.setObjectName("l_rs")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_rs)
        self.t_rs = QtWidgets.QLineEdit(self.w_depositar)
        self.t_rs.setObjectName("t_rs")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_rs)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.b_depositar = QtWidgets.QPushButton(self.w_depositar)
        self.b_depositar.setObjectName("b_depositar")
        self.gridLayout_2.addWidget(self.b_depositar, 0, 3, 1, 1)
        self.b_limpar_2 = QtWidgets.QPushButton(self.w_depositar)
        self.b_limpar_2.setObjectName("b_limpar_2")
        self.gridLayout_2.addWidget(self.b_limpar_2, 0, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.b_voltar_2 = QtWidgets.QPushButton(self.w_depositar)
        self.b_voltar_2.setObjectName("b_voltar_2")
        self.gridLayout_2.addWidget(self.b_voltar_2, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.w_operacoes = QtWidgets.QWidget(self.centralwidget)
        self.w_operacoes.setGeometry(QtCore.QRect(60, 90, 271, 221))
        self.w_operacoes.setObjectName("w_operacoes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.w_operacoes)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l_operacoes = QtWidgets.QLabel(self.w_operacoes)
        self.l_operacoes.setObjectName("l_operacoes")
        self.verticalLayout_5.addWidget(self.l_operacoes)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.b_sacar = QtWidgets.QPushButton(self.w_operacoes)
        self.b_sacar.setObjectName("b_sacar")
        self.verticalLayout_6.addWidget(self.b_sacar)
        self.b_depositar_2 = QtWidgets.QPushButton(self.w_operacoes)
        self.b_depositar_2.setObjectName("b_depositar_2")
        self.verticalLayout_6.addWidget(self.b_depositar_2)
        self.b_transferir = QtWidgets.QPushButton(self.w_operacoes)
        self.b_transferir.setObjectName("b_transferir")
        self.verticalLayout_6.addWidget(self.b_transferir)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.label = QtWidgets.QLabel(self.w_operacoes)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.b_sair = QtWidgets.QPushButton(self.w_operacoes)
        self.b_sair.setObjectName("b_sair")
        self.verticalLayout_5.addWidget(self.b_sair)

        self.w_transferir = QtWidgets.QWidget(self.centralwidget)
        self.w_transferir.setGeometry(QtCore.QRect(20, 60, 361, 251))
        self.w_transferir.setObjectName("w_transferir")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.w_transferir)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.l_rg_dest = QtWidgets.QLabel(self.w_transferir)
        self.l_rg_dest.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.l_rg_dest.setObjectName("l_rg_dest")
        self.verticalLayout_7.addWidget(self.l_rg_dest)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_5.setObjectName("formLayout_5")
        self.l_rg_2 = QtWidgets.QLabel(self.w_transferir)
        self.l_rg_2.setObjectName("l_rg_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_rg_2)
        self.t_rg_2 = QtWidgets.QLineEdit(self.w_transferir)
        self.t_rg_2.setObjectName("t_rg_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_rg_2)
        self.verticalLayout_7.addLayout(self.formLayout_5)
        self.l_valor = QtWidgets.QLabel(self.w_transferir)
        self.l_valor.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.l_valor.setObjectName("l_valor")
        self.verticalLayout_7.addWidget(self.l_valor)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_6.setObjectName("formLayout_6")
        self.l_rs_2 = QtWidgets.QLabel(self.w_transferir)
        self.l_rs_2.setObjectName("l_rs_2")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_rs_2)
        self.t_rs_2 = QtWidgets.QLineEdit(self.w_transferir)
        self.t_rs_2.setObjectName("t_rs_2")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_rs_2)
        self.verticalLayout_7.addLayout(self.formLayout_6)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.b_transferir_2 = QtWidgets.QPushButton(self.w_transferir)
        self.b_transferir_2.setObjectName("b_transferir_2")
        self.gridLayout_5.addWidget(self.b_transferir_2, 0, 3, 1, 1)
        self.b_limpar_4 = QtWidgets.QPushButton(self.w_transferir)
        self.b_limpar_4.setObjectName("b_limpar_4")
        self.gridLayout_5.addWidget(self.b_limpar_4, 0, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.b_voltar_4 = QtWidgets.QPushButton(self.w_transferir)
        self.b_voltar_4.setObjectName("b_voltar_4")
        self.gridLayout_5.addWidget(self.b_voltar_4, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)

        self.w_sacar = QtWidgets.QWidget(self.centralwidget)
        self.w_sacar.setGeometry(QtCore.QRect(20, 80, 361, 251))
        self.w_sacar.setObjectName("w_sacar")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.w_sacar)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.l_sacar = QtWidgets.QLabel(self.w_sacar)
        self.l_sacar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.l_sacar.setObjectName("l_sacar")
        self.verticalLayout_8.addWidget(self.l_sacar)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_7.setObjectName("formLayout_7")
        self.l_rs_3 = QtWidgets.QLabel(self.w_sacar)
        self.l_rs_3.setObjectName("l_rs_3")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_rs_3)
        self.t_rs_3 = QtWidgets.QLineEdit(self.w_sacar)
        self.t_rs_3.setObjectName("t_rs_3")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_rs_3)
        self.verticalLayout_8.addLayout(self.formLayout_7)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.b_sacar_2 = QtWidgets.QPushButton(self.w_sacar)
        self.b_sacar_2.setObjectName("b_sacar_2")
        self.gridLayout_7.addWidget(self.b_sacar_2, 0, 3, 1, 1)
        self.b_limpar_5 = QtWidgets.QPushButton(self.w_sacar)
        self.b_limpar_5.setObjectName("b_limpar_5")
        self.gridLayout_7.addWidget(self.b_limpar_5, 0, 2, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        self.b_voltar_5 = QtWidgets.QPushButton(self.w_sacar)
        self.b_voltar_5.setObjectName("b_voltar_5")
        self.gridLayout_7.addWidget(self.b_voltar_5, 0, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_7)

        self.w_saldo = QtWidgets.QWidget(self.centralwidget)
        self.w_saldo.setGeometry(QtCore.QRect(130, 160, 160, 80))
        self.w_saldo.setObjectName("w_saldo")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.w_saldo)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.l_saldo = QtWidgets.QLabel(self.w_saldo)
        self.l_saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_saldo.setObjectName("l_saldo")
        self.verticalLayout_10.addWidget(self.l_saldo)
        self.b_ok = QtWidgets.QPushButton(self.w_saldo)
        self.b_ok.setObjectName("b_ok")
        self.verticalLayout_10.addWidget(self.b_ok)

        self.w_erro = QtWidgets.QWidget(self.centralwidget)
        self.w_erro.setGeometry(QtCore.QRect(130, 160, 160, 80))
        self.w_erro.setObjectName("w_erro")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.w_erro)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.l_erro = QtWidgets.QLabel(self.w_erro)
        self.l_erro.setAlignment(QtCore.Qt.AlignCenter)
        self.l_erro.setObjectName("l_erro")
        self.verticalLayout_11.addWidget(self.l_erro)
        self.b_ok_2 = QtWidgets.QPushButton(self.w_erro)
        self.b_ok_2.setObjectName("b_ok_2")
        self.verticalLayout_11.addWidget(self.b_ok_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.w_bemvindo.show()
        self.w_login.hide()
        self.w_cadastro.hide()
        self.w_depositar.hide()
        self.w_operacoes.hide()
        self.w_transferir.hide()
        self.w_sacar.hide()
        self.w_saldo.hide()
        self.w_erro.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ### Essa função renomeia todas as labels e títulos que a aplicação possui ###
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_login.setText(_translate("MainWindow", "Login"))
        self.b_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.l_rg.setText(_translate("MainWindow", "Insira o seu RG"))
        self.b_entrar_login.setText(_translate("MainWindow", "Entrar"))
        self.b_limpar_login.setText(_translate("MainWindow", "Limpar"))
        self.b_voltar_login.setText(_translate("MainWindow", "Voltar"))
        self.l_rg_3.setText(_translate("MainWindow", "Insira o seu RG"))
        self.l_nome_2.setText(_translate("MainWindow", "Insira o seu nome"))
        self.b_entrar_cadastro.setText(_translate("MainWindow", "Entrar"))
        self.b_limpar_cadastro.setText(_translate("MainWindow", "Limpar"))
        self.b_voltar_cadastro.setText(_translate("MainWindow", "Voltar"))
        self.l_deposito.setText(_translate("MainWindow", "Insira o valor que deseja depositar:"))
        self.l_rs.setText(_translate("MainWindow", "R$"))
        self.b_depositar.setText(_translate("MainWindow", "Depositar"))
        self.b_limpar_2.setText(_translate("MainWindow", "Limpar"))
        self.b_voltar_2.setText(_translate("MainWindow", "Voltar"))
        self.l_operacoes.setText(_translate("MainWindow", "O que você deseja, "))
        self.b_sacar.setText(_translate("MainWindow", "Sacar"))
        self.b_depositar_2.setText(_translate("MainWindow", "Depositar"))
        self.b_transferir.setText(_translate("MainWindow", "Transferir"))
        self.label.setText(_translate("MainWindow", "Saldo: R$ "))

        self.b_sair.setText(_translate("MainWindow", "Sair"))
        self.l_rg_dest.setText(_translate("MainWindow", "Insira o RG do destinatário:"))
        self.l_rg_2.setText(_translate("MainWindow", "RG"))
        self.l_valor.setText(_translate("MainWindow", "Insira o valor que deseja transferir:"))
        self.l_rs_2.setText(_translate("MainWindow", "R$"))
        self.b_transferir_2.setText(_translate("MainWindow", "Transferir"))
        self.b_limpar_4.setText(_translate("MainWindow", "Limpar"))
        self.b_voltar_4.setText(_translate("MainWindow", "Voltar"))
        self.l_sacar.setText(_translate("MainWindow", "Insira o valor que deseja sacar:"))
        self.l_rs_3.setText(_translate("MainWindow", "R$"))
        self.b_sacar_2.setText(_translate("MainWindow", "Sacar"))
        self.b_limpar_5.setText(_translate("MainWindow", "Limpar"))
        self.b_voltar_5.setText(_translate("MainWindow", "Voltar"))
        self.l_saldo.setText(_translate("MainWindow", "saldo"))
        self.b_ok.setText(_translate("MainWindow", "OK!"))
        self.l_erro.setText(_translate("MainWindow", "erro"))
        self.b_ok_2.setText(_translate("MainWindow", "OK!"))