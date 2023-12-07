# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 430)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Screens = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.Screens.setGeometry(QtCore.QRect(0, 0, 501, 431))
        self.Screens.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.Screens.setObjectName("Screens")
        self.Pick = QtWidgets.QWidget()
        self.Pick.setObjectName("Pick")
        self.C_ONE = QtWidgets.QRadioButton(parent=self.Pick)
        self.C_ONE.setGeometry(QtCore.QRect(10, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_ONE.setFont(font)
        self.C_ONE.setObjectName("C_ONE")
        self.C_TWO = QtWidgets.QRadioButton(parent=self.Pick)
        self.C_TWO.setGeometry(QtCore.QRect(10, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_TWO.setFont(font)
        self.C_TWO.setObjectName("C_TWO")
        self.C_THREE = QtWidgets.QRadioButton(parent=self.Pick)
        self.C_THREE.setGeometry(QtCore.QRect(10, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_THREE.setFont(font)
        self.C_THREE.setObjectName("C_THREE")
        self.START = QtWidgets.QPushButton(parent=self.Pick)
        self.START.setGeometry(QtCore.QRect(150, 320, 161, 41))
        self.START.setCheckable(True)
        self.START.setObjectName("START")
        self.PICK = QtWidgets.QLabel(parent=self.Pick)
        self.PICK.setGeometry(QtCore.QRect(150, 0, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PICK.setFont(font)
        self.PICK.setScaledContents(True)
        self.PICK.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PICK.setObjectName("PICK")
        self.label = QtWidgets.QLabel(parent=self.Pick)
        self.label.setGeometry(QtCore.QRect(180, 50, 111, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("A.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.Pick)
        self.label_2.setGeometry(QtCore.QRect(180, 140, 111, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("B.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.Pick)
        self.label_3.setGeometry(QtCore.QRect(180, 230, 111, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.Stats_Label = QtWidgets.QLabel(parent=self.Pick)
        self.Stats_Label.setGeometry(QtCore.QRect(340, 50, 111, 81))
        self.Stats_Label.setStyleSheet("background-color: rgb(252, 76, 2);")
        self.Stats_Label.setText("")
        self.Stats_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Stats_Label.setObjectName("Stats_Label")
        self.Stats_Label_2 = QtWidgets.QLabel(parent=self.Pick)
        self.Stats_Label_2.setGeometry(QtCore.QRect(340, 140, 111, 81))
        self.Stats_Label_2.setStyleSheet("background-color: rgb(5, 194, 221);")
        self.Stats_Label_2.setText("")
        self.Stats_Label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Stats_Label_2.setObjectName("Stats_Label_2")
        self.Stats_Label_3 = QtWidgets.QLabel(parent=self.Pick)
        self.Stats_Label_3.setGeometry(QtCore.QRect(340, 230, 111, 81))
        self.Stats_Label_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.Stats_Label_3.setText("")
        self.Stats_Label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Stats_Label_3.setObjectName("Stats_Label_3")
        self.Screens.addWidget(self.Pick)
        self.Battle = QtWidgets.QWidget()
        self.Battle.setObjectName("Battle")
        self.BATTLETITLE = QtWidgets.QLabel(parent=self.Battle)
        self.BATTLETITLE.setGeometry(QtCore.QRect(50, 0, 111, 31))
        self.BATTLETITLE.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.BATTLETITLE.setObjectName("BATTLETITLE")
        self.PLAYER_STATS = QtWidgets.QLabel(parent=self.Battle)
        self.PLAYER_STATS.setGeometry(QtCore.QRect(10, 150, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.PLAYER_STATS.setFont(font)
        self.PLAYER_STATS.setText("")
        self.PLAYER_STATS.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.PLAYER_STATS.setObjectName("PLAYER_STATS")
        self.ENEMY_STATS = QtWidgets.QLabel(parent=self.Battle)
        self.ENEMY_STATS.setGeometry(QtCore.QRect(190, 20, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ENEMY_STATS.setFont(font)
        self.ENEMY_STATS.setText("")
        self.ENEMY_STATS.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.ENEMY_STATS.setObjectName("ENEMY_STATS")
        self.PLAYER_IMAGE = QtWidgets.QLabel(parent=self.Battle)
        self.PLAYER_IMAGE.setGeometry(QtCore.QRect(140, 150, 121, 91))
        self.PLAYER_IMAGE.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.PLAYER_IMAGE.setText("")
        self.PLAYER_IMAGE.setScaledContents(True)
        self.PLAYER_IMAGE.setObjectName("PLAYER_IMAGE")
        self.ENEMY_IMAGE = QtWidgets.QLabel(parent=self.Battle)
        self.ENEMY_IMAGE.setGeometry(QtCore.QRect(320, 20, 121, 91))
        self.ENEMY_IMAGE.setText("")
        self.ENEMY_IMAGE.setScaledContents(True)
        self.ENEMY_IMAGE.setObjectName("ENEMY_IMAGE")
        self.BATTLEOPTIONS = QtWidgets.QLabel(parent=self.Battle)
        self.BATTLEOPTIONS.setGeometry(QtCore.QRect(310, 250, 131, 21))
        self.BATTLEOPTIONS.setObjectName("BATTLEOPTIONS")
        self.CURRENT_EVENT = QtWidgets.QLabel(parent=self.Battle)
        self.CURRENT_EVENT.setGeometry(QtCore.QRect(10, 310, 251, 51))
        self.CURRENT_EVENT.setText("")
        self.CURRENT_EVENT.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CURRENT_EVENT.setObjectName("CURRENT_EVENT")
        self.PLAYERO = QtWidgets.QStackedWidget(parent=self.Battle)
        self.PLAYERO.setGeometry(QtCore.QRect(310, 280, 161, 81))
        self.PLAYERO.setObjectName("PLAYERO")
        self.BOPTIONS = QtWidgets.QWidget()
        self.BOPTIONS.setObjectName("BOPTIONS")
        self.ATTACK = QtWidgets.QPushButton(parent=self.BOPTIONS)
        self.ATTACK.setGeometry(QtCore.QRect(0, 10, 71, 31))
        self.ATTACK.setObjectName("ATTACK")
        self.QUIT = QtWidgets.QPushButton(parent=self.BOPTIONS)
        self.QUIT.setGeometry(QtCore.QRect(80, 10, 71, 31))
        self.QUIT.setObjectName("QUIT")
        self.PLAYERO.addWidget(self.BOPTIONS)
        self.MOVES = QtWidgets.QWidget()
        self.MOVES.setObjectName("MOVES")
        self.MOVE = QtWidgets.QPushButton(parent=self.MOVES)
        self.MOVE.setGeometry(QtCore.QRect(0, 10, 71, 31))
        self.MOVE.setText("")
        self.MOVE.setObjectName("MOVE")
        self.MOVE_2 = QtWidgets.QPushButton(parent=self.MOVES)
        self.MOVE_2.setGeometry(QtCore.QRect(70, 10, 71, 31))
        self.MOVE_2.setStyleSheet("")
        self.MOVE_2.setText("")
        self.MOVE_2.setObjectName("MOVE_2")
        self.MOVE_3 = QtWidgets.QPushButton(parent=self.MOVES)
        self.MOVE_3.setGeometry(QtCore.QRect(0, 40, 71, 31))
        self.MOVE_3.setAutoFillBackground(False)
        self.MOVE_3.setText("")
        self.MOVE_3.setDefault(False)
        self.MOVE_3.setFlat(False)
        self.MOVE_3.setObjectName("MOVE_3")
        self.BACK = QtWidgets.QPushButton(parent=self.MOVES)
        self.BACK.setGeometry(QtCore.QRect(70, 40, 71, 31))
        self.BACK.setObjectName("BACK")
        self.PLAYERO.addWidget(self.MOVES)
        self.CURRENT_EVENT_2 = QtWidgets.QLabel(parent=self.Battle)
        self.CURRENT_EVENT_2.setGeometry(QtCore.QRect(10, 250, 251, 61))
        self.CURRENT_EVENT_2.setText("")
        self.CURRENT_EVENT_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CURRENT_EVENT_2.setObjectName("CURRENT_EVENT_2")
        self.HPBAR_ONE = QtWidgets.QProgressBar(parent=self.Battle)
        self.HPBAR_ONE.setGeometry(QtCore.QRect(10, 200, 118, 16))
        self.HPBAR_ONE.setAcceptDrops(False)
        self.HPBAR_ONE.setAutoFillBackground(False)
        self.HPBAR_ONE.setProperty("value", 100)
        self.HPBAR_ONE.setObjectName("HPBAR_ONE")
        self.HPBAR_ONE_2 = QtWidgets.QProgressBar(parent=self.Battle)
        self.HPBAR_ONE_2.setGeometry(QtCore.QRect(190, 70, 118, 16))
        self.HPBAR_ONE_2.setProperty("value", 100)
        self.HPBAR_ONE_2.setObjectName("HPBAR_ONE_2")
        self.Turn_Tracker = QtWidgets.QLabel(parent=self.Battle)
        self.Turn_Tracker.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.Turn_Tracker.setObjectName("Turn_Tracker")
        self.Conclusion = QtWidgets.QLabel(parent=self.Battle)
        self.Conclusion.setGeometry(QtCore.QRect(320, 170, 141, 41))
        self.Conclusion.setText("")
        self.Conclusion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Conclusion.setObjectName("Conclusion")
        self.Screens.addWidget(self.Battle)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Screens.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BattleSimulator"))
        self.C_ONE.setText(_translate("MainWindow", "BLITZADILE"))
        self.C_TWO.setText(_translate("MainWindow", "JORMANGANDR"))
        self.C_THREE.setText(_translate("MainWindow", "TOTOGAIA"))
        self.START.setText(_translate("MainWindow", "START BATTLE!!!"))
        self.PICK.setText(_translate("MainWindow", "Pick a Character"))
        self.BATTLETITLE.setText(_translate("MainWindow", "Battle Screen"))
        self.BATTLEOPTIONS.setText(_translate("MainWindow", "Battle Options"))
        self.ATTACK.setText(_translate("MainWindow", "Attack"))
        self.QUIT.setText(_translate("MainWindow", "Quit"))
        self.BACK.setText(_translate("MainWindow", "BACK"))
        self.Turn_Tracker.setText(_translate("MainWindow", "Turn: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
