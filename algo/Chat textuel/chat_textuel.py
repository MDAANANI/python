
#1
'''
message = 'nsi'
octets = message.encode("Utf8")
print(type(octets))
print(octets)
'''
'''
octets = b'nsi'
message = octets.decode()
print(type(message))
print(message)
'''


#3
'''
#serveur UDP (CTRL+F2 pour stopper)
import socket

UDP_IP_MON_PC = " 172.18.50.162"   #adresse de mon serveur
UDP_PORT_MON_PC = 5000        #port de mon serveur

# Crée un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

boucle=True
while(boucle):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data=None
            continue
        print ('received ', data)
        if (data.decode()=='q'):
            boucle=False
print('closing socket')
sock.close()
'''

#5

#Chat texte en UDP sans QUdpSocket

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import socket

UDP_IP_DU_BINOME = "127.0.0.1"   #adresse du client (la machine du binôme) à adapter
UDP_PORT_DU_BINOME = 5000        #port du client (la machine du binôme) à adapter

UDP_IP_MON_PC = "127.0.0.1"   #adresse de mon serveur
UDP_PORT_MON_PC = 5000        #port de mon serveur

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('chat-pyqt.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()                     #affiche la fenêtre MainWindows

        self.pushButton_envoyer.clicked.connect(self.boutonEnvoi)
        self.timer = QTimer(self)   #déclaration du timer
        self.timer.timeout.connect(self.miseAJour) #déclenche la méthode mise à jour
        self.timer.start(100)      #toutes les secondes (100ms)

    def miseAJour(self):
        try:
            octets, serveur = sock.recvfrom(1024)
        except socket.error or msg :
            octets=None
        if octets!=None:
            message=octets.decode()
            print('reception :',message)
            self.listwidget.insertItem(0,message)
            self.listwidget.item(0).setForeground(QtCore.Qt.blue)


    def boutonEnvoi(self):
        msg=self.lineEdit_msg.text()
        print('texte envoyé.',msg)
        octets = msh.encode("Utf8")
        print(octets)

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()