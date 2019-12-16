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
        self.timer_count2 = 0
        self.count = 0
        self.count2 = 0
        self.timerVar2 = 0
        self.timerVar1 = 0


    def execute(self, obj, event):
        if self.timerVar1 == 0:
            self.actor.SetPosition(0, self.timer_count, 420)
            if self.count == 1:
                self.timer_count += 1

            if self.timer_count > 500 and self.count == 1:
                self.count = 2

            if self.count == 3:
                self.timer_count -= 1

            if self.timer_count < -500 and self.count == 3:
                self.count = 2

            iren = obj
            iren.Initialize()


        if self.timerVar1 == 1:
            self.actor.SetPosition(0, self.timer_count, 420)
            iren = obj
            iren.Initialize()

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
            iren = obj
            iren.Initialize()

        if self.timerVar2 == 1:
            self.actor.RotateY(0)
            iren = obj
            iren.Initialize()

    def execute3(self, obj, event):
        if self.timerVar1 == 0:
            self.actor.SetPosition(760, self.timer_count, 220)
            if self.count == 1:
                self.timer_count += 1

            if self.timer_count > 500 and self.count == 1:
                self.count = 2

            if self.count == 3:
                self.timer_count -= 1

            if self.timer_count < -500 and self.count == 3:
                self.count = 2

            iren = obj
            iren.Initialize()

        if self.timerVar1 == 1:
            self.actor.SetPosition(760, self.timer_count, 220)
            iren = obj
            iren.Initialize()

    def execute4(self, obj, event):
        if self.timerVar1 == 0:
            self.actor.SetPosition(-760, self.timer_count, 220)
            if self.count == 1:
                self.timer_count += 1

            if self.timer_count > 500 and self.count == 1:
                self.count = 2

            if self.count == 3:
                self.timer_count -= 1

            if self.timer_count < -500 and self.count == 3:
                self.count = 2

            iren = obj
            iren.Initialize()

        if self.timerVar1 == 1:
            self.actor.SetPosition(-760, self.timer_count, 220)
            iren = obj
            iren.Initialize()

    def execute5(self, obj, event):
        if self.timerVar1 == 0:
            self.actor.SetPosition(0, self.timer_count-25, 500+self.timer_count2)
            if self.count == 1:
                self.timer_count += 1

            if self.timer_count > 500 and self.count == 1:
                self.count = 2

            if self.count == 3:
                self.timer_count -= 1

            if self.timer_count < -500 and self.count == 3:
                self.count = 2

            iren = obj
            iren.Initialize()

        if self.timerVar1 == 1:
            self.actor.SetPosition(0, self.timer_count-25, 500+self.timer_count2)
            iren = obj
            iren.Initialize()

    def execute6(self, obj, event):
        if self.timerVar2 == 0:
            self.actor.SetPosition(0, self.timer_count-25, 500+self.timer_count2)
            if self.count2 == 1:
                self.timer_count2 += 1

            if self.timer_count2 > 200 and self.count2 == 1:
                self.count2 = 2

            if self.count2 == 3:
                self.timer_count2 -= 1

            if self.timer_count2 < -200 and self.count2 == 3:
                self.count2 = 2

            iren = obj
            iren.Initialize()

        if self.timerVar1 == 1:
            self.actor.SetPosition(0, self.timer_count-25, 500+self.timer_count2)
            iren = obj
            iren.Initialize()

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
        # source = vtk.vtkSphereSource()
        # source.SetCenter(0, 0, 0)
        # source.SetRadius(5.0)

        source = vtk.vtkCubeSource()
        source.SetXLength(1500)
        source.SetYLength(1500)
        source.SetZLength(100)
        source.SetCenter(0, 0, 0)

        source2 = vtk.vtkCubeSource()
        source2.SetXLength(25)
        source2.SetYLength(200)
        source2.SetZLength(550)
        source2.SetCenter(0, 0, 0)

        source3 = vtk.vtkCubeSource()
        source3.SetXLength(1500)
        source3.SetYLength(25)
        source3.SetZLength(150)
        source2.SetCenter(0, 0, 0)

        source4 = vtk.vtkCubeSource()
        source4.SetXLength(200)
        source4.SetYLength(25)
        source4.SetZLength(550)
        source4.SetCenter(0, 0, 0)



        filename = "/Users/steve/PycharmProjects/vtktest/CylinderHead-stl/CylinderHead-binary.stl"
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        reader.Update()

        # Create a mapper
        #mapperSTL = vtk.vtkPolyDataMapper()
        #mapperSTL.SetInputConnection(reader.GetOutputPort())
        mapperBase = vtk.vtkPolyDataMapper()
        mapperBase.SetInputConnection(source.GetOutputPort())
        mapperBase2 = vtk.vtkPolyDataMapper()
        mapperBase2.SetInputConnection(source2.GetOutputPort())
        mapperBase3 = vtk.vtkPolyDataMapper()
        mapperBase3.SetInputConnection(source2.GetOutputPort())
        mapperBase4 = vtk.vtkPolyDataMapper()
        mapperBase4.SetInputConnection(source3.GetOutputPort())
        mapperBase5 = vtk.vtkPolyDataMapper()
        mapperBase5.SetInputConnection(source4.GetOutputPort())

        # Create an actor
        #STLactor = vtk.vtkActor()
        #STLactor.SetMapper(mapperSTL)
        BaseActor = vtk.vtkActor()
        BaseActor.SetMapper(mapperBase)
        BaseActor.SetPosition((0, 0, 0))
        BaseActor.GetProperty().SetColor(1.0,0,0)
        #STLactor.SetScale(5,5,5)
        BaseActor2 = vtk.vtkActor()
        BaseActor2.SetMapper(mapperBase2)
        BaseActor2.GetProperty().SetColor(0, 0, 1.0)
        BaseActor2.SetPosition(760,0,180)
        BaseActor3 = vtk.vtkActor()
        BaseActor3.SetMapper(mapperBase3)
        BaseActor3.GetProperty().SetColor(0, 0, 1.0)
        BaseActor3.SetPosition(-760, 0, 180)
        BaseActor4 = vtk.vtkActor()
        BaseActor4.SetMapper(mapperBase4)
        BaseActor4.GetProperty().SetColor(0, 0, 1.0)
        BaseActor4.SetPosition(0, 0, 380)
        BaseActor5 = vtk.vtkActor()
        BaseActor5.SetMapper(mapperBase5)
        BaseActor5.GetProperty().SetColor(1.0, 1.0, 0)
        BaseActor5.SetPosition(0, -25, 500)

        #self.ren.AddActor(STLactor)
        self.ren.AddActor(BaseActor)
        self.ren.AddActor(BaseActor2)
        self.ren.AddActor(BaseActor3)
        self.ren.AddActor(BaseActor4)
        self.ren.AddActor(BaseActor5)


        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        # self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()
        # put timer event here

        cbBase2 = vtkTimerCallback()
        cbBase3 = vtkTimerCallback()
        cbBase4 = vtkTimerCallback()
        cbBase5 = vtkTimerCallback()
        cbBase2.actor = BaseActor2
        cbBase3.actor = BaseActor3
        cbBase4.actor = BaseActor4
        cbBase5.actor = BaseActor5
        #cbSTL = vtkTimerCallback()
        #cbSTL.actor = STLactor

        def getfiles():
            try:
                file = QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.stl')
                if file == None:
                  file = "/Users/steve/PycharmProjects/vtktest/CylinderHead-stl/CylinderHead-binary.stl"
                str = file[0]
                reader.SetFileName(str)
                reader.Update()
                #mapper.SetInputConnection(reader.GetOutputPort())
                #STLactor.SetMapper(mapper)
            except Exception as e:
                print("Exception in method")
                print(e)

        def stopR():
            cbSTL.timerVar2 = 1

        def startR():
            cbSTL.timerVar2 = 0

        def stopY():
            cbBase2.timerVar1 = 1
            cbBase3.timerVar1 = 1
            cbBase4.timerVar1 = 1
            cbBase5.timerVar1 = 1

        def forwardY():
            cbBase2.timerVar1 = 0
            cbBase3.timerVar1 = 0
            cbBase4.timerVar1 = 0
            cbBase5.timerVar1 = 0
            cbBase2.count = 3
            cbBase3.count = 3
            cbBase4.count = 3
            cbBase5.count = 3

        def backY():
            cbBase2.timerVar1 = 0
            cbBase3.timerVar1 = 0
            cbBase4.timerVar1 = 0
            cbBase5.timerVar1 = 0
            cbBase2.count = 1
            cbBase3.count = 1
            cbBase4.count = 1
            cbBase5.count = 1

        def upZ():
            cbBase5.timerVar2 = 0
            cbBase5.count2 = 1

        def downZ():
            cbBase5.timerVar2 = 0
            cbBase5.count2 = 3

        def stopZ():
            cbBase5.timerVar2 = 1
            cbBase5.count2 = 2

        #self.vtkWidget.AddObserver('TimerEvent', cbSTL.execute2)
        self.vtkWidget.AddObserver('TimerEvent', cbBase2.execute3)
        self.vtkWidget.AddObserver('TimerEvent', cbBase3.execute4)
        self.vtkWidget.AddObserver('TimerEvent', cbBase4.execute)
        self.vtkWidget.AddObserver('TimerEvent', cbBase5.execute5)
        self.vtkWidget.AddObserver('TimerEvent', cbBase5.execute6)

        #self.stopRotationButton.clicked.connect(stopR)
        #self.startRotationButton.clicked.connect(startR)
        try:
            self.STLButton.clicked.connect(getfiles)
        except Exception as ex:
            print("Exception in button call")
            print(ex)
        self.stopYButton.clicked.connect(stopY)
        self.forwardYButton.clicked.connect(forwardY)
        self.backYButton.clicked.connect(backY)
        self.stopZButton.clicked.connect(stopZ)
        self.upZButton.clicked.connect(upZ)
        self.downZButton.clicked.connect(downZ)

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
