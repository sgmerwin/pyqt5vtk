import vtk
import sys
import os
import psutil
import math

from PyQt5 import QtCore
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QWidget
from foo import Ui4_MainWindow
from PyQt5 import Qt
import threading

def memory():
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss / math.pow(10, 6))

thread1 = threading.Thread(target=memory())

class vtkTimerCallback():
    def __init__(self):
        self.timer_count = 0
        self.count = 0
        self.timerVar2 = 0
        self.timerVar1 = 0

    def execute(self, obj, event):
        if self.timerVar1 == 0:
            self.actor.SetPosition(self.timer_count, self.timer_count, 0)
            if self.count == 0:
                self.timer_count += 1

            if self.timer_count > 200:
                self.count = 1
            if self.count == 1:
                self.timer_count -= 1

            if self.timer_count < -200:
                self.count = 0

        if self.timerVar1 == 1:
            self.actor.SetPosition(self.timer_count, self.timer_count, 0)

    def execute2(self, obj, event):
        if self.timerVar2 == 0:
            # self.actor.RotateX(self.timer_count)
            self.actor.RotateY(self.timer_count)
            # self.actor.RotateZ(self.timer_count)
            if self.count == 0:
                self.timer_count -= .01
            if self.timer_count < -2:
                self.count = 1
                # self.timer_count = 0
            if self.count == 1:
                self.timer_count += .01
            if self.timer_count > 2:
                self.count = 0

        if self.timerVar2 == 1:
            self.actor.RotateY(0)

class MainWindow(QMainWindow, Ui4_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.OpenVTK()
        self.update()

    def update(self):
        self.width = self.width()
        self.height = self.height()
        self.frame.setGeometry(self.width/2, 0, self.width/2, self.height)

    def OpenVTK(self):
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl = Qt.QVBoxLayout()
        self.vl.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)

        filename = "/Users/steve/PycharmProjects/vtktest/CylinderHead-stl/CylinderHead-binary.stl"
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        reader.Update()

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())
        mapper2 = vtk.vtkPolyDataMapper()
        mapper2.SetInputConnection(source.GetOutputPort())

        # Create an actor
        STLactor = vtk.vtkActor()
        STLactor.SetMapper(mapper)
        sphereactor = vtk.vtkActor()
        sphereactor.SetMapper(mapper2)
        sphereactor.SetPosition((100, 100, 100))

        self.ren.AddActor(STLactor)
        self.ren.AddActor(sphereactor)

        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        # self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()
        # put timer event here

        cbSphere = vtkTimerCallback()
        cbSphere.actor = sphereactor
        cbSTL = vtkTimerCallback()
        cbSTL.actor = STLactor

        def getfiles():
            try:
                file = QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.stl')
                if file == None:
                  file = "/Users/steve/PycharmProjects/vtktest/CylinderHead-stl/CylinderHead-binary.stl"
                str = file[0]
                reader.SetFileName(str)
                reader.Update()
                mapper.SetInputConnection(reader.GetOutputPort())
                STLactor.SetMapper(mapper)
            except Exception as e:
                print("Exception in method")
                print(e)

        def stopR():
            cbSTL.timerVar2 = 1

        def startR():
            cbSTL.timerVar2 = 0

        def stopL():
            cbSphere.timerVar1 = 1

        def startL():
            cbSphere.timerVar1 = 0

        self.vtkWidget.AddObserver('TimerEvent', cbSTL.execute2)
        self.vtkWidget.AddObserver('TimerEvent', cbSphere.execute)
        self.stopRotationButton.clicked.connect(stopR)
        self.startRotationButton.clicked.connect(startR)
        try:
            self.STLButton.clicked.connect(getfiles)
        except Exception as ex:
            print("Exception in button call")
            print(ex)
        self.stopLinearButton.clicked.connect(stopL)
        self.startLinearButton.clicked.connect(startL)

        self.vtkWidget.CreateRepeatingTimer(1)

        self.iren.Start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    thread1.start()
    print("thread 1")
    memory()
    print("main thread")
    sys.exit(app.exec_())
