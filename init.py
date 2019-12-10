import vtk
import sys
from PyQt5 import QtCore, QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from foo import Ui_MainWindow
from PyQt5 import Qt
import threading
import time

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
        if self.timer_count == 200:
            self.count = 1
        if self.count == 1:
            self.timer_count -= 1
        if self.timer_count == -200:
            self.count = 0

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.OpenVTK)
        self.OpenVTK()

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
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor2 = vtk.vtkActor()
        actor2.SetMapper(mapper2)
        actor2.SetPosition((100, 100, 100))


        # def runA():
        #     while True:
        #         actor2.SetPosition((-100,-100,0))
        #         time.sleep(4)
        #         actor2.SetPosition((100, 100, 100))
        #         time.sleep(4)
        #
        # t1 = threading.Thread(target = runA)
        # t1.setDaemon(True)
        # t1.start()

        self.ren.AddActor(actor)
        self.ren.AddActor(actor2)

        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        #self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()
        #put timer event here

        cb = vtkTimerCallback()
        cb.actor = actor2
        self.vtkWidget.AddObserver('TimerEvent', cb.execute)
        self.vtkWidget.CreateRepeatingTimer(1)


        self.iren.Start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())