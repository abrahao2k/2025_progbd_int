# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="ifrn")
cursor = conexao.cursor()
print("Conexao OK")

class Ui_CadAluno(object):
    def setupUi(self, CadAluno):
        CadAluno.setObjectName("CadAluno")
        CadAluno.resize(270, 220)
        self.centralwidget = QtWidgets.QWidget(CadAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.label_turno = QtWidgets.QLabel(self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.gridLayout.addWidget(self.label_turno, 2, 0, 1, 1)
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)
        self.label_extra = QtWidgets.QLabel(self.centralwidget)
        self.label_extra.setObjectName("label_extra")
        self.gridLayout.addWidget(self.label_extra, 3, 0, 1, 1)
        self.label_obs = QtWidgets.QLabel(self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 4, 0, 1, 1)
        self.comboBox_curso = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_curso.setObjectName("comboBox_curso")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.gridLayout.addWidget(self.comboBox_curso, 1, 1, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.plainTextEdit_obs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_obs.setObjectName("plainTextEdit_obs")
        self.gridLayout.addWidget(self.plainTextEdit_obs, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_manha = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_manha.setObjectName("radio_manha")
        self.horizontalLayout.addWidget(self.radio_manha)
        self.radio_tarde = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_tarde.setObjectName("radio_tarde")
        self.horizontalLayout.addWidget(self.radio_tarde)
        self.radio_noite = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_noite.setObjectName("radio_noite")
        self.horizontalLayout.addWidget(self.radio_noite)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_atleta = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_atleta.setObjectName("checkBox_atleta")
        self.horizontalLayout_2.addWidget(self.checkBox_atleta)
        self.checkBox_bolsista = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_bolsista.setObjectName("checkBox_bolsista")
        self.horizontalLayout_2.addWidget(self.checkBox_bolsista)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar) # <<<<<<<
        
        self.gridLayout.addWidget(self.pushButton_salvar, 5, 1, 1, 1)
        CadAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadAluno)
        QtCore.QMetaObject.connectSlotsByName(CadAluno)

    def retranslateUi(self, CadAluno):
        _translate = QtCore.QCoreApplication.translate
        CadAluno.setWindowTitle(_translate("CadAluno", "Cadastro de Aluno"))
        self.label_nome.setText(_translate("CadAluno", "Nome:"))
        self.label_turno.setText(_translate("CadAluno", "Turno:"))
        self.label_curso.setText(_translate("CadAluno", "Curso:"))
        self.label_extra.setText(_translate("CadAluno", "Extra:"))
        self.label_obs.setText(_translate("CadAluno", "Obs.:"))
        self.comboBox_curso.setItemText(0, _translate("CadAluno", "Edificações"))
        self.comboBox_curso.setItemText(1, _translate("CadAluno", "Eletrotécnica"))
        self.comboBox_curso.setItemText(2, _translate("CadAluno", "Informática"))
        self.comboBox_curso.setItemText(3, _translate("CadAluno", "Mecânica"))
        self.radio_manha.setText(_translate("CadAluno", "Manhã"))
        self.radio_tarde.setText(_translate("CadAluno", "Tarde"))
        self.radio_noite.setText(_translate("CadAluno", "Noite"))
        self.checkBox_atleta.setText(_translate("CadAluno", "Atleta"))
        self.checkBox_bolsista.setText(_translate("CadAluno", "Bolsista"))
        self.pushButton_salvar.setText(_translate("CadAluno", "SALVAR"))


    def salvar(self):
        nome = self.lineEdit_nome.text()
        curso = self.comboBox_curso.currentText()
        
        turno =  ""
        if   self.radio_manha.isChecked(): turno = "Manhã"
        elif self.radio_tarde.isChecked(): turno = "Tarde"
        elif self.radio_noite.isChecked(): turno = "Noite"
        
        atleta = "Não"
        if self.checkBox_atleta.isChecked(): atleta = "Sim"
        
        bolsista = "Não"
        if self.checkBox_bolsista.isChecked(): bolsista = "Sim"
        
        obs = self.plainTextEdit_obs.toPlainText()
        
        sql=f'''INSERT INTO alunos VALUES(null,'{nome}', '{curso}',
                '{turno}', '{atleta}', '{bolsista}', '{obs}')'''
        cursor.execute(sql)
        conexao.commit()
        print("INSERIDO COM SUCESSO")
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadAluno = QtWidgets.QMainWindow()
    ui = Ui_CadAluno()
    ui.setupUi(CadAluno)
    CadAluno.show()
    sys.exit(app.exec_())