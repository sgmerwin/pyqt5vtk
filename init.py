import vtk
import sys
import os
import psutil
import math

from PyQt5 import QtCore, QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from foo import Ui_MainWindow
from PyQt5 import Qt
import threading
import time


def memory():
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss / math.pow(10, 6))

thread1 = threading.Thread(target=memory())

class vtkTimerCallback():
    def __init__(self):
        self.timer_count = 0
        self.count = 0

    def execute(self, obj, event):
        self.actor.SetPosition(self.timer_count, self.timer_count, 0)

        iren = obj
        iren.GetRenderWindow().Render()
        if self.count == 0:
            self.timer_count += 1

        if self.timer_count > 200:
            self.count = 1
        if self.count == 1:
            self.timer_count -= 1

        if self.timer_count < -200:
            self.count = 0

    def execute2(self, obj, event):
        # self.actor.RotateX(self.timer_count)
        self.actor.RotateY(self.timer_count)
        # self.actor.RotateZ(self.timer_count)

        iren = obj
        iren.GetRenderWindow().Render()
        if self.count == 0:
            self.timer_count -= .01
        if self.timer_count < -2:
            self.count = 1
            # self.timer_count = 0
        if self.count == 1:
            self.timer_count += .01
        if self.timer_count > 2:
            self.count = 0

    def execute3(self, obj, event):
        self.actor.RotateX(0)
        self.actor.RotateY(0)
        self.actor.RotateZ(0)

        iren = obj
        iren.GetRenderWindow().Render()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.OpenVTK()
        # self.pushButton.clicked.connect(self.OpenVTK)

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



        def stop():
            rotation.RemoveObservers('TimerEvent')
            rotation.AddObserver('TimerEvent', cbSphere.execute)

        def start():
            self.vtkWidget.AddObserver('TimerEvent', cbSTL.execute2)

        self.vtkWidget.AddObserver('TimerEvent', cbSTL.execute2)
        self.vtkWidget.AddObserver('TimerEvent', cbSphere.execute)
        rotation = self.vtkWidget
        self.stopButton.clicked.connect(stop)
        self.startButton.clicked.connect(start)

        self.vtkWidget.CreateRepeatingTimer(100)

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
