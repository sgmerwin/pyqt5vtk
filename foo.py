from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLayout.setStretchFactor(self.frame, 1)
        self.horizontalLayout.setStretchFactor(self.stopButton, 1)
        self.horizontalLayout.setStretchFactor(self.startButton, 1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stopButton.setText(_translate("MainWindow", "StopRotation"))
        self.startButton.setText(_translate("MainWindow", "StartRotation"))

class Ui4_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.horizontalLayout.addLayout(self.verticalLayout,0)

        self.stopRotationButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopRotationButton.setText("Stop Rotation")
        self.verticalLayout.addWidget(self.stopRotationButton)
        self.stopRotationButton.move(0,0)

        self.startRotationButton = QtWidgets.QPushButton(self.centralwidget)
        self.startRotationButton.setText("Start Rotation")
        self.verticalLayout.addWidget(self.startRotationButton)
        self.startRotationButton.move(1,0)

        self.STLButton = QtWidgets.QPushButton(self.centralwidget)
        self.STLButton.setText("Load STL")
        self.verticalLayout.addWidget(self.STLButton)
        self.STLButton.move(2,0)

        self.stopYButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopYButton.setText("Stop Y")
        self.verticalLayout.addWidget(self.stopYButton)
        self.stopYButton.move(3,0)

        self.forwardYButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardYButton.setText("Forward Y")
        self.verticalLayout.addWidget(self.forwardYButton)
        self.forwardYButton.move(4, 0)

        self.backYButton = QtWidgets.QPushButton(self.centralwidget)
        self.backYButton.setText("back Y")
        self.verticalLayout.addWidget(self.backYButton)
        self.backYButton.move(5, 0)

        self.upZButton = QtWidgets.QPushButton(self.centralwidget)
        self.upZButton.setText("Up Z")
        self.verticalLayout.addWidget(self.upZButton)
        self.upZButton.move(6, 0)

        self.downZButton = QtWidgets.QPushButton(self.centralwidget)
        self.downZButton.setText("Down Z")
        self.verticalLayout.addWidget(self.downZButton)
        self.downZButton.move(7, 0)

        self.stopZButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopZButton.setText("Stop Z")
        self.verticalLayout.addWidget(self.stopZButton)
        self.stopZButton.move(8, 0)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame.move(0,1)
        self.horizontalLayout.setStretchFactor(self.verticalLayout,1)
        self.horizontalLayout.setStretchFactor(self.frame, 4)

        MainWindow.setCentralWidget(self.centralwidget)




