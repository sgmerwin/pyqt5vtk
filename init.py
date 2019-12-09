import vtk
import sys
from PyQt5 import QtCore, QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from foo import Ui_MainWindow
from PyQt5 import Qt

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

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.ren.AddActor(actor)

        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        #self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()
        self.iren.Start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())