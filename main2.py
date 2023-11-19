from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt
import sys
import random
from outrosArquivos.janela2 import ClasseJanela

app = QApplication(sys.argv)
janela = ClasseJanela()
janela.setFixedSize(800,600)
janela.setWindowTitle("Jogo do Trânsito")
janela.show()
app.exec()