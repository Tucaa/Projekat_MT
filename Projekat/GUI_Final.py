import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from datetime import timedelta
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

    #Konstruktor. Generalno kada se .ui fajl konvertuje u .py dobije se klasa bez konstruktora __init__(bude samo def setupUi(self, MainWindow).
    #Program radi sa i bez konstruktora
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(MainWindow)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 909)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Podloga = QtWidgets.QLabel(self.centralwidget)
        self.Podloga.setGeometry(QtCore.QRect(0, 0, 1071, 511))
        self.Podloga.setText("")
        self.Podloga.setPixmap(QtGui.QPixmap("C:\PyProjekti_Milan\OSNOVA-a_copy"))
        self.Podloga.setScaledContents(True)
        self.Podloga.setObjectName("Podloga")
        self.sto1 = QtWidgets.QPushButton(self.centralwidget)
        self.sto1.setGeometry(QtCore.QRect(892, 360, 35, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto1.setFont(font)
        self.sto1.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto1.setObjectName("sto1")
        self.sto2 = QtWidgets.QPushButton(self.centralwidget)
        self.sto2.setGeometry(QtCore.QRect(988, 360, 35, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto2.setFont(font)
        self.sto2.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto2.setObjectName("sto2")
        self.sto8 = QtWidgets.QPushButton(self.centralwidget)
        self.sto8.setGeometry(QtCore.QRect(692, 360, 35, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto8.setFont(font)
        self.sto8.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto8.setObjectName("sto8")
        self.sto9 = QtWidgets.QPushButton(self.centralwidget)
        self.sto9.setGeometry(QtCore.QRect(596, 360, 35, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto9.setFont(font)
        self.sto9.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto9.setObjectName("sto9")
        self.sto10 = QtWidgets.QPushButton(self.centralwidget)
        self.sto10.setGeometry(QtCore.QRect(692, 288, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto10.setFont(font)
        self.sto10.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto10.setObjectName("sto10")
        self.sto3 = QtWidgets.QPushButton(self.centralwidget)
        self.sto3.setGeometry(QtCore.QRect(892, 288, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto3.setFont(font)
        self.sto3.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto3.setObjectName("sto3")
        self.sto4 = QtWidgets.QPushButton(self.centralwidget)
        self.sto4.setGeometry(QtCore.QRect(988, 288, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto4.setFont(font)
        self.sto4.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto4.setObjectName("sto4")
        self.sto11 = QtWidgets.QPushButton(self.centralwidget)
        self.sto11.setGeometry(QtCore.QRect(596, 288, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto11.setFont(font)
        self.sto11.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto11.setObjectName("sto11")
        self.sto32 = QtWidgets.QPushButton(self.centralwidget)
        self.sto32.setGeometry(QtCore.QRect(347, 410, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto32.setFont(font)
        self.sto32.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto32.setObjectName("sto32")
        self.sto31 = QtWidgets.QPushButton(self.centralwidget)
        self.sto31.setGeometry(QtCore.QRect(445, 410, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto31.setFont(font)
        self.sto31.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto31.setObjectName("sto31")
        self.sto33 = QtWidgets.QPushButton(self.centralwidget)
        self.sto33.setGeometry(QtCore.QRect(250, 410, 35, 47))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto33.setFont(font)
        self.sto33.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto33.setObjectName("sto33")
        self.sto30 = QtWidgets.QPushButton(self.centralwidget)
        self.sto30.setGeometry(QtCore.QRect(902, 424, 30, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto30.setFont(font)
        self.sto30.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto30.setObjectName("sto30")
        self.sto29 = QtWidgets.QPushButton(self.centralwidget)
        self.sto29.setGeometry(QtCore.QRect(962, 424, 30, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto29.setFont(font)
        self.sto29.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto29.setObjectName("sto29")
        self.sto28 = QtWidgets.QPushButton(self.centralwidget)
        self.sto28.setGeometry(QtCore.QRect(1012, 424, 30, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto28.setFont(font)
        self.sto28.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto28.setObjectName("sto28")
        self.sto13 = QtWidgets.QPushButton(self.centralwidget)
        self.sto13.setGeometry(QtCore.QRect(596, 210, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto13.setFont(font)
        self.sto13.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto13.setObjectName("sto13")
        self.sto12 = QtWidgets.QPushButton(self.centralwidget)
        self.sto12.setGeometry(QtCore.QRect(706, 210, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto12.setFont(font)
        self.sto12.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto12.setObjectName("sto12")
        self.sto5 = QtWidgets.QPushButton(self.centralwidget)
        self.sto5.setGeometry(QtCore.QRect(892, 210, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto5.setFont(font)
        self.sto5.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto5.setObjectName("sto5")
        self.sto6 = QtWidgets.QPushButton(self.centralwidget)
        self.sto6.setGeometry(QtCore.QRect(986, 210, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto6.setFont(font)
        self.sto6.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto6.setObjectName("sto6")
        self.sto16 = QtWidgets.QPushButton(self.centralwidget)
        self.sto16.setGeometry(QtCore.QRect(437, 214, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto16.setFont(font)
        self.sto16.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto16.setObjectName("sto16")
        self.sto17 = QtWidgets.QPushButton(self.centralwidget)
        self.sto17.setGeometry(QtCore.QRect(344, 214, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto17.setFont(font)
        self.sto17.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto17.setObjectName("sto17")
        self.sto24 = QtWidgets.QPushButton(self.centralwidget)
        self.sto24.setGeometry(QtCore.QRect(239, 214, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto24.setFont(font)
        self.sto24.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto24.setObjectName("sto24")
        self.sto7 = QtWidgets.QPushButton(self.centralwidget)
        self.sto7.setGeometry(QtCore.QRect(948, 60, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto7.setFont(font)
        self.sto7.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto7.setObjectName("sto7")
        self.sto26 = QtWidgets.QPushButton(self.centralwidget)
        self.sto26.setGeometry(QtCore.QRect(196, 105, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto26.setFont(font)
        self.sto26.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto26.setObjectName("sto26")
        self.sto27 = QtWidgets.QPushButton(self.centralwidget)
        self.sto27.setGeometry(QtCore.QRect(73, 105, 27, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto27.setFont(font)
        self.sto27.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto27.setObjectName("sto27")
        self.sto25 = QtWidgets.QPushButton(self.centralwidget)
        self.sto25.setGeometry(QtCore.QRect(38, 218, 85, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto25.setFont(font)
        self.sto25.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto25.setObjectName("sto25")
        self.sto14 = QtWidgets.QPushButton(self.centralwidget)
        self.sto14.setGeometry(QtCore.QRect(374, 315, 108, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto14.setFont(font)
        self.sto14.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto14.setObjectName("sto14")
        self.sto15 = QtWidgets.QPushButton(self.centralwidget)
        self.sto15.setGeometry(QtCore.QRect(298, 315, 53, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto15.setFont(font)
        self.sto15.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto15.setObjectName("sto15")
        self.sto23 = QtWidgets.QPushButton(self.centralwidget)
        self.sto23.setGeometry(QtCore.QRect(33, 327, 26, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto23.setFont(font)
        self.sto23.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto23.setObjectName("sto23")
        self.sto22 = QtWidgets.QPushButton(self.centralwidget)
        self.sto22.setGeometry(QtCore.QRect(80, 327, 26, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto22.setFont(font)
        self.sto22.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto22.setObjectName("sto22")
        self.sto21 = QtWidgets.QPushButton(self.centralwidget)
        self.sto21.setGeometry(QtCore.QRect(111, 327, 26, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto21.setFont(font)
        self.sto21.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto21.setObjectName("sto21")
        self.sto20 = QtWidgets.QPushButton(self.centralwidget)
        self.sto20.setGeometry(QtCore.QRect(161, 327, 26, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto20.setFont(font)
        self.sto20.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto20.setObjectName("sto20")
        self.sto19 = QtWidgets.QPushButton(self.centralwidget)
        self.sto19.setGeometry(QtCore.QRect(190, 327, 26, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto19.setFont(font)
        self.sto19.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto19.setObjectName("sto19")
        self.sto18 = QtWidgets.QPushButton(self.centralwidget)
        self.sto18.setGeometry(QtCore.QRect(239, 327, 26, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sto18.setFont(font)
        self.sto18.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.sto18.setObjectName("sto18")
        self.StatusTabela = QtWidgets.QTableWidget(self.centralwidget)
        self.StatusTabela.setGeometry(QtCore.QRect(0, 510, 645, 400))
        self.StatusTabela.setObjectName("StatusTabela")
        self.StatusTabela.setColumnCount(6)
        self.StatusTabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTabela.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTabela.setHorizontalHeaderItem(5, item)
        self.Ime = QtWidgets.QLabel(self.centralwidget)
        self.Ime.setGeometry(QtCore.QRect(670, 565, 51, 20))
        self.Ime.setObjectName("Ime")
        self.br_osoba = QtWidgets.QLabel(self.centralwidget)
        self.br_osoba.setGeometry(QtCore.QRect(670, 605, 81, 20))
        self.br_osoba.setObjectName("br_osoba")
        self.Ime_Rez = QtWidgets.QLineEdit(self.centralwidget)
        self.Ime_Rez.setGeometry(QtCore.QRect(760, 565, 131, 20))
        self.Ime_Rez.setObjectName("Ime_Rez")
        self.broj_osoba = QtWidgets.QLineEdit(self.centralwidget)
        self.broj_osoba.setGeometry(QtCore.QRect(760, 605, 31, 20))
        self.broj_osoba.setObjectName("broj_osoba")
        self.Br_slobodnih_stolova = QtWidgets.QLabel(self.centralwidget)
        self.Br_slobodnih_stolova.setGeometry(QtCore.QRect(670, 685, 141, 16))
        self.Br_slobodnih_stolova.setObjectName("Br_slobodnih_stolova")
        self.br_slobodnih = QtWidgets.QTextBrowser(self.centralwidget)
        self.br_slobodnih.setGeometry(QtCore.QRect(780, 680, 51, 23))
        self.br_slobodnih.setObjectName("br_slobodnih")
        self.Uslovi_za_rezervaciju = QtWidgets.QLabel(self.centralwidget)
        self.Uslovi_za_rezervaciju.setGeometry(QtCore.QRect(670, 535, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Uslovi_za_rezervaciju.setFont(font)
        self.Uslovi_za_rezervaciju.setObjectName("Uslovi_za_rezervaciju")
        self.clear_unos = QtWidgets.QPushButton(self.centralwidget)
        self.clear_unos.setGeometry(QtCore.QRect(800, 605, 91, 20))
        self.clear_unos.setObjectName("clear_unos")
        self.poruka = QtWidgets.QTextBrowser(self.centralwidget)
        self.poruka.setGeometry(QtCore.QRect(670, 755, 381, 61))
        self.poruka.setObjectName("poruka")
        self.prozor_za_por = QtWidgets.QLabel(self.centralwidget)
        self.prozor_za_por.setGeometry(QtCore.QRect(670, 725, 111, 20))
        self.prozor_za_por.setObjectName("prozor_za_por")
        self.clear_poruka = QtWidgets.QPushButton(self.centralwidget)
        self.clear_poruka.setGeometry(QtCore.QRect(960, 825, 91, 20))
        self.clear_poruka.setObjectName("clear_poruka")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(300, 10, 171, 25))
        self.lcdNumber.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.lcdNumber.setObjectName("lcdNumber")
        self.Radno_vreme = QtWidgets.QLabel(self.centralwidget)
        self.Radno_vreme.setGeometry(QtCore.QRect(20, 15, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Radno_vreme.setFont(font)
        self.Radno_vreme.setObjectName("Radno_vreme")
        self.trenutno_stanje = QtWidgets.QLabel(self.centralwidget)
        self.trenutno_stanje.setGeometry(QtCore.QRect(0, 490, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trenutno_stanje.setFont(font)
        self.trenutno_stanje.setObjectName("trenutno_stanje")
        MainWindow.setCentralWidget(self.centralwidget)

        #Timer:
        self.timer = QTimer()
        self.timer.timeout.connect(self.digitalni_sat)
        self.timer.start(1000)
        self.digitalni_sat()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Pozivanje svih funkcija

        self.ucitavanje_sql()
        self.clear_unos.clicked.connect(self.unos_clear)
        self.clear_poruka.clicked.connect(self.poruka_clear)


        # Sto1
        self.sto1.clicked.connect(lambda: self.broj_osoba_rez(self.sto1))
        self.status_stola(self.sto1)
        self.sto1.clicked.connect(lambda: self.pop_up(self.sto1))

        # Sto2
        self.sto2.clicked.connect(lambda: self.broj_osoba_rez(self.sto2))
        self.status_stola(self.sto2)
        self.sto2.clicked.connect(lambda: self.pop_up(self.sto2))

        # Sto3
        self.sto3.clicked.connect(lambda: self.broj_osoba_rez(self.sto3))
        self.status_stola(self.sto3)
        self.sto3.clicked.connect(lambda: self.pop_up(self.sto3))

        # Sto4
        self.sto4.clicked.connect(lambda: self.broj_osoba_rez(self.sto4))
        self.status_stola(self.sto4)
        self.sto4.clicked.connect(lambda: self.pop_up(self.sto4))

        # Sto5
        self.sto5.clicked.connect(lambda: self.broj_osoba_rez(self.sto5))
        self.status_stola(self.sto5)
        self.sto5.clicked.connect(lambda: self.pop_up(self.sto5))

        # Sto6
        self.sto6.clicked.connect(lambda: self.broj_osoba_rez(self.sto6))
        self.status_stola(self.sto6)
        self.sto6.clicked.connect(lambda: self.pop_up(self.sto6))

        # Sto7
        self.sto7.clicked.connect(lambda: self.broj_osoba_rez(self.sto7))
        self.status_stola(self.sto7)
        self.sto7.clicked.connect(lambda: self.pop_up(self.sto7))

        # Sto8
        self.sto8.clicked.connect(lambda: self.broj_osoba_rez(self.sto8))
        self.status_stola(self.sto8)
        self.sto8.clicked.connect(lambda: self.pop_up(self.sto8))

        # Sto9
        self.sto9.clicked.connect(lambda: self.broj_osoba_rez(self.sto9))
        self.status_stola(self.sto9)
        self.sto9.clicked.connect(lambda: self.pop_up(self.sto9))

        # Sto10
        self.sto10.clicked.connect(lambda: self.broj_osoba_rez(self.sto10))
        self.status_stola(self.sto10)
        self.sto10.clicked.connect(lambda: self.pop_up(self.sto10))

        # Sto11
        self.sto11.clicked.connect(lambda: self.broj_osoba_rez(self.sto11))
        self.status_stola(self.sto11)
        self.sto11.clicked.connect(lambda: self.pop_up(self.sto11))

        # Sto12
        self.sto12.clicked.connect(lambda: self.broj_osoba_rez(self.sto12))
        self.status_stola(self.sto12)
        self.sto12.clicked.connect(lambda: self.pop_up(self.sto12))

        # Sto13
        self.sto13.clicked.connect(lambda: self.broj_osoba_rez(self.sto13))
        self.status_stola(self.sto13)
        self.sto13.clicked.connect(lambda: self.pop_up(self.sto13))

        # Sto14
        self.sto14.clicked.connect(lambda: self.broj_osoba_rez(self.sto14))
        self.status_stola(self.sto14)
        self.sto14.clicked.connect(lambda: self.pop_up(self.sto14))

        # Sto15
        self.sto15.clicked.connect(lambda: self.broj_osoba_rez(self.sto15))
        self.status_stola(self.sto15)
        self.sto15.clicked.connect(lambda: self.pop_up(self.sto15))

        # Sto16
        self.sto16.clicked.connect(lambda: self.broj_osoba_rez(self.sto16))
        self.status_stola(self.sto16)
        self.sto16.clicked.connect(lambda: self.pop_up(self.sto16))

        # Sto17
        self.sto17.clicked.connect(lambda: self.broj_osoba_rez(self.sto17))
        self.status_stola(self.sto17)
        self.sto17.clicked.connect(lambda: self.pop_up(self.sto17))

        # Sto18
        self.sto18.clicked.connect(lambda: self.broj_osoba_rez(self.sto18))
        self.status_stola(self.sto18)
        self.sto18.clicked.connect(lambda: self.pop_up(self.sto18))

        # Sto19
        self.sto19.clicked.connect(lambda: self.broj_osoba_rez(self.sto19))
        self.status_stola(self.sto19)
        self.sto19.clicked.connect(lambda: self.pop_up(self.sto19))

        # Sto20
        self.sto20.clicked.connect(lambda: self.broj_osoba_rez(self.sto20))
        self.status_stola(self.sto20)
        self.sto20.clicked.connect(lambda: self.pop_up(self.sto20))

        # Sto21
        self.sto21.clicked.connect(lambda: self.broj_osoba_rez(self.sto21))
        self.status_stola(self.sto21)
        self.sto21.clicked.connect(lambda: self.pop_up(self.sto21))

        # Sto22
        self.sto22.clicked.connect(lambda: self.broj_osoba_rez(self.sto22))
        self.status_stola(self.sto22)
        self.sto22.clicked.connect(lambda: self.pop_up(self.sto22))

        # Sto23
        self.sto23.clicked.connect(lambda: self.broj_osoba_rez(self.sto23))
        self.status_stola(self.sto23)
        self.sto23.clicked.connect(lambda: self.pop_up(self.sto23))

        # Sto24
        self.sto24.clicked.connect(lambda: self.broj_osoba_rez(self.sto24))
        self.status_stola(self.sto24)
        self.sto24.clicked.connect(lambda: self.pop_up(self.sto24))

        # Sto25
        self.sto25.clicked.connect(lambda: self.broj_osoba_rez(self.sto25))
        self.status_stola(self.sto25)
        self.sto25.clicked.connect(lambda: self.pop_up(self.sto25))

        # Sto26
        self.sto26.clicked.connect(lambda: self.broj_osoba_rez(self.sto26))
        self.status_stola(self.sto26)
        self.sto26.clicked.connect(lambda: self.pop_up(self.sto26))

        # Sto27
        self.sto27.clicked.connect(lambda: self.broj_osoba_rez(self.sto27))
        self.status_stola(self.sto27)
        self.sto27.clicked.connect(lambda: self.pop_up(self.sto27))

        # Sto28
        self.sto28.clicked.connect(lambda: self.broj_osoba_rez(self.sto28))
        self.status_stola(self.sto28)
        self.sto28.clicked.connect(lambda: self.pop_up(self.sto28))

        # Sto29
        self.sto29.clicked.connect(lambda: self.broj_osoba_rez(self.sto29))
        self.status_stola(self.sto29)
        self.sto29.clicked.connect(lambda: self.pop_up(self.sto29))

        # Sto30
        self.sto30.clicked.connect(lambda: self.broj_osoba_rez(self.sto30))
        self.status_stola(self.sto30)
        self.sto30.clicked.connect(lambda: self.pop_up(self.sto30))

        # Sto31
        self.sto31.clicked.connect(lambda: self.broj_osoba_rez(self.sto31))
        self.status_stola(self.sto31)
        self.sto31.clicked.connect(lambda: self.pop_up(self.sto31))

        # Sto32
        self.sto32.clicked.connect(lambda: self.broj_osoba_rez(self.sto32))
        self.status_stola(self.sto32)
        self.sto32.clicked.connect(lambda: self.pop_up(self.sto32))

        # Sto33
        self.sto33.clicked.connect(lambda: self.broj_osoba_rez(self.sto33))
        self.status_stola(self.sto33)
        self.sto33.clicked.connect(lambda: self.pop_up(self.sto33))

        self.broj_slobodnih_stolova()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sto1.setText(_translate("MainWindow", "1"))
        self.sto2.setText(_translate("MainWindow", "2"))
        self.sto8.setText(_translate("MainWindow", "8"))
        self.sto9.setText(_translate("MainWindow", "9"))
        self.sto10.setText(_translate("MainWindow", "10"))
        self.sto3.setText(_translate("MainWindow", "3"))
        self.sto4.setText(_translate("MainWindow", "4"))
        self.sto11.setText(_translate("MainWindow", "11"))
        self.sto32.setText(_translate("MainWindow", "32"))
        self.sto31.setText(_translate("MainWindow", "31"))
        self.sto33.setText(_translate("MainWindow", "33"))
        self.sto30.setText(_translate("MainWindow", "30"))
        self.sto29.setText(_translate("MainWindow", "29"))
        self.sto28.setText(_translate("MainWindow", "28"))
        self.sto13.setText(_translate("MainWindow", "13"))
        self.sto12.setText(_translate("MainWindow", "12"))
        self.sto5.setText(_translate("MainWindow", "5"))
        self.sto6.setText(_translate("MainWindow", "6"))
        self.sto16.setText(_translate("MainWindow", "16"))
        self.sto17.setText(_translate("MainWindow", "17"))
        self.sto24.setText(_translate("MainWindow", "24"))
        self.sto7.setText(_translate("MainWindow", "7"))
        self.sto26.setText(_translate("MainWindow", "26"))
        self.sto27.setText(_translate("MainWindow", "27"))
        self.sto25.setText(_translate("MainWindow", "25"))
        self.sto14.setText(_translate("MainWindow", "14"))
        self.sto15.setText(_translate("MainWindow", "15"))
        self.sto23.setText(_translate("MainWindow", "23"))
        self.sto22.setText(_translate("MainWindow", "22"))
        self.sto21.setText(_translate("MainWindow", "21"))
        self.sto20.setText(_translate("MainWindow", "20"))
        self.sto19.setText(_translate("MainWindow", "19"))
        self.sto18.setText(_translate("MainWindow", "18"))
        item = self.StatusTabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "sto"))
        item = self.StatusTabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "br_mesta"))
        item = self.StatusTabela.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "status_stola"))
        item = self.StatusTabela.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "rezervacija"))
        item = self.StatusTabela.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "vreme_rezervacije"))
        item = self.StatusTabela.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "rezervisan_do"))
        self.Ime.setText(_translate("MainWindow", "Uneti Ime:"))
        self.br_osoba.setText(_translate("MainWindow", "Uneti br. osoba:"))
        self.Br_slobodnih_stolova.setText(_translate("MainWindow", "Br. slobodnih stolova:"))
        self.Uslovi_za_rezervaciju.setText(_translate("MainWindow", "Uslovi za rezervaciju"))
        self.clear_unos.setText(_translate("MainWindow", "clear"))
        self.prozor_za_por.setText(_translate("MainWindow", "PROZOR ZA PORUKU"))
        self.clear_poruka.setText(_translate("MainWindow", "clearexc"))
        self.Radno_vreme.setText(_translate("MainWindow", "Radno vreme: 08:00 - 00:00"))
        self.trenutno_stanje.setText(_translate("MainWindow", "Trenutno stanje:"))


    def digitalni_sat(self):
        vreme = datetime.now()
        f_vreme = vreme.strftime("%H:%M:%S")


        self.lcdNumber.setDigitCount(12)
        self.lcdNumber.display(f_vreme)


    def ucitavanje_sql(self):
        db = mysql.connector.connect(
           host='localhost',
           user='root',
           password='root',
           database='sql_baza_projekat'
       )

        my_cursor = db.cursor()
        #Querry za selektovanje tabele iz data baze
        my_cursor.execute("SELECT * FROM stolovi")

        self.StatusTabela.setRowCount(33)
        red_tabele = 0
        for row in my_cursor:
            #Pisanje u tabelu
            self.StatusTabela.setItem(red_tabele, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.StatusTabela.setItem(red_tabele, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.StatusTabela.setItem(red_tabele, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.StatusTabela.setItem(red_tabele, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.StatusTabela.setItem(red_tabele, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.StatusTabela.setItem(red_tabele, 5, QtWidgets.QTableWidgetItem(row[5]))

            red_tabele += 1

        return db


    def status_stola(self, sto):
        db = self.ucitavanje_sql()
        my_cursor = db.cursor()

        #Uzimanje brojas stola
        broj = sto.text()

        #Selektovanje kolone_status stola iz tabele stolovi
        my_cursor.execute(f'SELECT status_stola FROM stolovi WHERE id_stola = {broj}')

        #Uzimanje jednog elementa vraca tupl!
        status = my_cursor.fetchone()

        #Neophodno je indeksiranje posto je tupl u pitanju.
        if status[0] == "zauzet":
            sto.setStyleSheet("background-color: red")
            return 1

        return 0


    def broj_osoba_rez(self, sto):
        db = self.ucitavanje_sql()
        my_cursor = db.cursor()

        broj = sto.text()


        my_cursor.execute(f'SELECT br_mesta FROM stolovi WHERE id_stola = {broj}')
        mesta = my_cursor.fetchone()

        #Minimalan broj clanova koji je potrebno zadovoljiti za rezervaciju
        min_broj = int(mesta[0]) - 1


        try:
            if int(self.broj_osoba.text()) < min_broj:
                return 1
            elif int(self.broj_osoba.text()) > int(mesta[0]):
                return 2
            return 0
        except Exception:
            print("Nije unet broj osoba!")
            self.poruka.setPlainText("Exception: Nije unet broj osoba!")

    def uneto_ime(self):
        ime = self.Ime_Rez.text()
        #Uslov za prazan string
        if not ime:
            return 1
        return 0


    def pop_up(self, sto):
        #Formiranje pop up prozora
        msg = QMessageBox()
        msg.setWindowTitle("Rezervacija")
        msg.setText("Izabrati opciju za rezervaciju")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Reset|QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setDetailedText(f'Reset - dugme za ponistavanje rezervacije\n'
                            f'Ok - dugme za rezervisanje\n'
                            f'Cancel - dugme za otkazivanje radnje')
        #Exectutovanje
        x  = msg.exec_()

        #Uslovi koji odredjuju koje dugme je pritisnuto
        if x == QMessageBox.Ok:
            self.rezervisi(sto)

        elif x == QMessageBox.Reset:
            self.skidanje_rez(sto)



    def rezervisi(self, sto):

        db = self.ucitavanje_sql()
        my_cursor = db.cursor()

        # Trenutno vreme
        vreme = datetime.now()
        # Formatriranje trenutnog vremena
        tren_vreme = vreme.strftime("%H:%M")
        # Trajanje rezervacije stavljeno je da je 2h
        trajanje = datetime.now() + timedelta(hours=2)
        # Formatiranje isteka rezervacije dodavanjem 2h na trenutno vreme
        istek_rezerv = trajanje.strftime("%H:%M")



        broj = sto.text()
        #Pozivanje funkcija i upisivanje istih u tmp promenjive
        tmp1 = self.broj_osoba_rez(sto)
        tmp2 = self.status_stola(sto)
        tmp3 = self.uneto_ime()



        #Uslov koji utvrdjuje da li su zadovoljeni uslovi broja clanova i status stola
        try:
            if tmp1 == 0 and tmp2 == 0 and tmp3 == 0:

                #Pisanje u tabelu
                my_cursor.execute(f'UPDATE stolovi SET status_stola = "zauzet" WHERE id_stola = {broj};')
                my_cursor.execute(f'UPDATE stolovi SET rezervacija = "{self.Ime_Rez.text()}" WHERE id_stola = {broj};')
                my_cursor.execute(f'UPDATE stolovi SET vreme_rezervacije = "{tren_vreme}" WHERE id_stola = {broj};')
                my_cursor.execute(f'UPDATE stolovi SET rezervisan_do = "{istek_rezerv}" WHERE id_stola = {broj};')

                #Cuvanje promena u data bazi
                db.commit()

                #Pormena boje stola
                sto.setStyleSheet("background-color: red")

                #Ponovno pozivanje funkcije
                self.ucitavanje_sql()
                self.broj_slobodnih_stolova()

                #Ispisivanje poruke u prozor za tekst poruke
                self.poruka.setPlainText("Rezervisano!")

            #Uslov za nedovoljan broj osoba
            elif tmp1 == 1:
                self.poruka.setPlainText("Exception: Nedovoljan broj osoba za rezervaciju!")
                raise Exception("Nedovoljan broj osoba za rezervaciju!")



            #Uslov za prevelik broj osoba
            elif tmp1 == 2:
                self.poruka.setPlainText("Exception: Prevelik broj osoba za rezervaciju!")
                raise Exception("Prevelik broj osoba za rezervaciju!")


            #Uslov ako je sto vec rezervisan
            elif tmp2 == 1:
                self.poruka.setPlainText("Exception: Sto je vec rezervisan!")
                raise Exception("Sto je vec rezervisan!")

            elif tmp3 == 1:
                self.poruka.setPlainText("Exception: Nije uneto ime!")
                raise Exception("Nije uneto ime!!")

        except Exception as e:
            print(e)


    def skidanje_rez(self, sto):

        db = self.ucitavanje_sql()
        my_cursor = db.cursor()

        broj = sto.text()

        #Pisanje u tabelu
        #OVDE TREBA DA STAVIS EXCEPTION AKO STO NIJE REZERVISAN UOPSTE!!!!
        my_cursor.execute(f'UPDATE stolovi SET status_stola = "slobodan" WHERE id_stola = {broj};')
        my_cursor.execute(f'UPDATE stolovi SET rezervacija = "" WHERE id_stola = {broj};')
        my_cursor.execute(f'UPDATE stolovi SET vreme_rezervacije = "" WHERE id_stola = {broj};')
        my_cursor.execute(f'UPDATE stolovi SET rezervisan_do = "" WHERE id_stola = {broj};')
        db.commit()
        sto.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.ucitavanje_sql()
        self.broj_slobodnih_stolova()
        self.poruka.setPlainText("Skinuta rezervacija!")


    def broj_slobodnih_stolova(self):
        db = self.ucitavanje_sql()
        my_cursor = db.cursor()

        my_cursor.execute("SELECT * FROM stolovi")
        brojac = 0

        #Petlja za iteriranje kroz clanove liste
        for row in my_cursor:
            if row[2] == "slobodan":
                brojac += 1
        self.br_slobodnih.setPlainText(str(brojac))


    def unos_clear(self):
        self.Ime_Rez.clear()
        self.broj_osoba.clear()

    def poruka_clear(self):
        self.poruka.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
