# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Arquivo convertido em ui2py.vercel.app


from PyQt5 import QtCore, QtGui, QtWidgets

import mariadb

conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="agenda")

cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(247, 153)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.label_fone = QtWidgets.QLabel(self.centralwidget)
        self.label_fone.setObjectName("label_fone")
        self.gridLayout.addWidget(self.label_fone, 1, 0, 1, 1)
        self.lineEdit_fone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fone.setObjectName("lineEdit_fone")
        self.gridLayout.addWidget(self.lineEdit_fone, 1, 1, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_fone.setText(_translate("MainWindow", "Telefone:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "SALVAR"))

    def salvar(self):
        nome = self.lineEdit_nome.text()
        fone = self.lineEdit_fone.text()
        sql = f"INSERT INTO pessoas VALUES (null, '{nome}', '{fone}')"
        cursor.execute(sql)
        conexao.commit()
        print("INSERIDO COM SUCESSO.")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
