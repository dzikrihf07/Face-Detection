import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from tkinter import *
from tkinter.filedialog import askopenfilename


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Kelompok 10 UAS Kecerdasan Buatan'
        self.left = 10
        self.top = 50
        self.width = 450
        self.height = 300
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button1 = QPushButton('Pilih Gambar', self)
        button1.setToolTip('Pilih gambar dengan maks ukuran resolusi layar anda')
        button1.setGeometry (QtCore.QRect(180, 200, 90, 40))
        button1.clicked.connect(self.OpenClick)

        font = QtGui.QFont()
        font.setPointSize(20)
        label1 = QLabel('Aplikasi Face Detection Kelompok 10', self)
        label1.setFont(font)
        label1.setGeometry (QtCore.QRect(10, 5, 450, 61))
        
        
        self.show()

    def OpenClick(self):
        self.FunctionUAS()


    def FunctionUAS(self):

        fileName = askopenfilename(filetypes = (("Gambar", "*.jpg*"),("Gambar", "*.png*"),("All files", "*.*")))
        b = fileName

        
        # Get user supplied values   
        cascPath = "haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(b)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 70, 255), 2)
         
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        textPosition           = (30,50)
        fontScale              = 1
        fontColor              = (0,0,0)
        lineType               = 3
         
        cv2.putText(image,"Mendapatkan {0} wajah!".format(len(faces)), 
            textPosition, 
            font, 
            fontScale,
            fontColor,
            lineType)

        print("Mendapatkan {0} wajah!".format(len(faces)))


        cv2.imshow("Kelompok 10 UAS Kecerdasan Buatan", image)
        cv2.waitKey(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    

    
