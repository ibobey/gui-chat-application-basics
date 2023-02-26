#pyQt5 Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon    
import sys
#Socket Connections
import socket
from socket import AF_INET,SOCK_STREAM
from threading import Thread

HOST = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDR = (HOST,PORT)
BUFFERSIZE = 1024
FORMAT = 'ascii'


class Ui_Form(object):

    nickname = ""

    def __init__(self) -> None:
        pass

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(481, 750)
        #Form.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        Form.setWindowOpacity(1.0)
        Form.setWindowIcon(QIcon("logo.png"))
        Form.setFixedSize(481, 750)


        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 731))
        self.widget.setObjectName("widget")


        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")


        self.label_user = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_user.setFont(font)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setObjectName("label_user")
        self.gridLayout.addWidget(self.label_user, 2, 1, 1, 1)


        self.textEdit_messageBox = QtWidgets.QTextEdit(self.widget)
        self.textEdit_messageBox.setObjectName("textEdit_messageBox")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(9)
        font.setWeight(75)
        self.textEdit_messageBox.setFont(font)
        self.textEdit_messageBox.setText("[PANDORA7 SERVER]")
        self.textEdit_messageBox.append("Choose a nickname ... ")
        self.textEdit_messageBox.setReadOnly(True)
        self.gridLayout.addWidget(self.textEdit_messageBox, 1, 0, 1, 3)


        self.pushButton_3_reconnect = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_reconnect.setFont(font)
        self.pushButton_3_reconnect.setObjectName("pushButton_3_reconnect")
        self.pushButton_3_reconnect.clicked.connect(self.buttonF_reconnect)
        self.gridLayout.addWidget(self.pushButton_3_reconnect, 4, 2, 1, 1)


        self.pushButton_2_clear = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2_clear.setFont(font)
        self.pushButton_2_clear.setObjectName("pushButton_2_clear")
        self.pushButton_2_clear.clicked.connect(self.buttonF_clear)
        self.gridLayout.addWidget(self.pushButton_2_clear, 4, 1, 1, 1)


        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)


        self.pushButton_send = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send.setFont(font)
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_send.clicked.connect(self.buttonF_send)
        self.gridLayout.addWidget(self.pushButton_send, 4, 0, 1, 1)


        self.pushButton_4_quit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4_quit.setFont(font)
        self.pushButton_4_quit.setObjectName("pushButton_4_quit")
        self.gridLayout.addWidget(self.pushButton_4_quit, 7, 1, 1, 1)
        self.pushButton_4_quit.clicked.connect(self.buttonF_quit)


        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 2, 1, 1)


        self.label_title = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PANDORA7"))
        self.label_user.setText(_translate("Form", "YOU"))
        self.pushButton_3_reconnect.setText(_translate("Form", "CONNECT"))
        self.pushButton_2_clear.setText(_translate("Form", "CLEAR"))
        self.pushButton_send.setText(_translate("Form", "SEND"))
        self.pushButton_4_quit.setText(_translate("Form", "QUIT"))
        self.label_2.setText(_translate("Form", ""))
        self.label_title.setText(_translate("Form", "PANDORA 7"))


    def buttonF_reconnect(self):
        if self.nickname == "":
            self.nickname = self.lineEdit.text()
            self.textEdit_messageBox.append(f"Your Nickname: {self.nickname}")
            self.lineEdit.clear()
            self.label_user.setText(self.nickname)
        
        try:
            self.client = socket.socket(AF_INET,SOCK_STREAM)
            self.client.connect(ADDR)
            receive_Thread = Thread(target=self.receiveServer)
            receive_Thread.start()

        except socket.error as E:
            self.textEdit_messageBox.append("[SOCKET ERROR !!!]")
            self.textEdit_messageBox.append("[CAN'T CONNECTED to SERVER.]")

    def receiveServer(self):
        self.client.send(self.nickname.encode(FORMAT))
        while True:
            try:
                message = self.client.recv(BUFFERSIZE).decode(FORMAT)
                self.textEdit_messageBox.append(message)
            except:
                self.textEdit_messageBox.append("[SERVER ERROR!]")
                self.client.close()
                break
                    

    def buttonF_send(self):
        message = self.lineEdit.text()
        message2 = f"{self.nickname}: {message}"
        self.client.send(message2.encode(FORMAT))
        
    def buttonF_clear(self):
        self.textEdit_messageBox.clear()
        self.lineEdit.clear()

    def buttonF_quit(self):
        Form.close()
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
