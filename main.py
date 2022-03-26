from PyQt5 import Qt

import sys
import os
import random

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPixmap, QFont
from PyQt5 import QtCore

from pdfminer.high_level import extract_text
import docx

def save_pdf_in_txt(path):
    txt = extract_text(path)

    print(txt)

    with open('file.txt', 'w+') as file:
        file.write(txt)
        file.close()


def save_pdf_in_word(path):
    txt = extract_text(path)

    print(txt)

    doc = docx.Document()
    par1 = doc.add_paragraph('Импортированно из pdf')

    par1.add_run(txt)

    doc.save('sample.docx')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        u = QGridLayout(self)

        self.btn = QPushButton('Конвертировать', self)
        self.btn.clicked.connect(self.k)
        self.btn.setFont(QFont("Times", 14))
        self.btn.setStyleSheet(
            "background-color: {}".format('#00c8ff'))
        self.btn.setMaximumSize(140000, 140000)
        u.addWidget(self.btn, 0, 0)
    
        '''self.name_input = QLineEdit(self)
        self.name_input.setText(str(a)[2:-3])
        self.name_input.setDisabled(True)
        self.name_input.setFont(QFont("Times", 18))
        self.name_input.setStyleSheet(
            "background-color: {}".format('#fff833'))
        self.name_input.setMaximumSize(140000, 140000)
        u.addWidget(self.name_input, 0, 0, 1, 3)'''
        
    def k(self):
        self.cwd = os.getcwd()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "Выбрать файл",  
                                    self.cwd, 
                                    "All Files (*);;Text Files (*.txt)")
        print(fileName_choose)
        fileName_choose1, filetype = QFileDialog.getOpenFileName(self,  
                                    "Выбрать файл",  
                                    self.cwd, 
                                    "All Files (*);;Text Files (*.txt)")
        print(fileName_choose1)

if __name__ == "__main__":
    app = Qt.QApplication([])
    t = Example()
    t.show()
    app.exec_()
