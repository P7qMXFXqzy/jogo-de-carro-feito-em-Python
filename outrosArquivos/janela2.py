from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt
import sys
import random
import math

class ClasseJanela (QWidget):
    enderecoYCarro = 367
    posicaoInimigo = 801
    moverInimigo1 = moverInimigo2 = moverInimigo3 = False
    velocidade = 1
    contagemPassos = 0
    sequencia = None

    def __init__(self):
        super(ClasseJanela, self).__init__()
        pixmapEstrada = QPixmap('outrosArquivos\\imagens\\estrada.png')
        imagemEstrada = QLabel(self)
        imagemEstrada.setPixmap(pixmapEstrada)
        imagemEstrada.setGeometry(0, 239, pixmapEstrada.width(), pixmapEstrada.height())
        pixmapGrama = QPixmap('outrosArquivos\\imagens\\grama.png')
        imagemGrama = QLabel(self)
        imagemGrama.setPixmap(pixmapGrama)
        imagemGrama.setGeometry(0, 121, pixmapGrama.width(), pixmapGrama.height())
        pixmapCeu = QPixmap('outrosArquivos\\imagens\\ceu.png')
        imagemCeu = QLabel(self)
        imagemCeu.setPixmap(pixmapCeu)
        imagemCeu.setGeometry(0, 0, pixmapCeu.width(), pixmapCeu.height())
        pixmapCarro = QPixmap('outrosArquivos\\imagens\\carro1.png')
        global imagemCarro
        imagemCarro = QLabel(self)
        imagemCarro.setPixmap(pixmapCarro)
        imagemCarro.setGeometry(6, self.enderecoYCarro, pixmapCarro.width(), pixmapCarro.height())
        pixmapInimigo1 = QPixmap('outrosArquivos\\imagens\\carro21.png')
        imagemInimigo1 = QLabel(self)
        imagemInimigo1.setPixmap(pixmapInimigo1)
        imagemInimigo1.setGeometry(801, 242, pixmapInimigo1.width(), pixmapInimigo1.height())
        imagemInimigo2 = QLabel(self)
        imagemInimigo2.setPixmap(pixmapInimigo1)
        imagemInimigo2.setGeometry(801, 367, pixmapInimigo1.width(), pixmapInimigo1.height())
        imagemInimigo3 = QLabel(self)
        imagemInimigo3.setPixmap(pixmapInimigo1)
        imagemInimigo3.setGeometry(801, 493, pixmapInimigo1.width(), pixmapInimigo1.height())

        def checarGameOver():
            retorno = False
            if(imagemInimigo1.x() < 217 and imagemInimigo1.x() > (-205)):
                if(imagemCarro.y() == imagemInimigo1.y()):
                    retorno = True
            elif(imagemInimigo2.x() < 217 and imagemInimigo2.x() > (-205)):
                if(imagemCarro.y() == imagemInimigo2.y()):
                    retorno = True
            elif(imagemInimigo3.x() < 217 and imagemInimigo3.x() > (-205)):
                if(imagemCarro.y() == imagemInimigo3.y()):
                    retorno = True
            return retorno
        
        #função pra movimentar os inimigos
        def movimentar():
            if(self.moverInimigo1 == self.moverInimigo2 == self.moverInimigo3 == False):
                self.sequencia = random.randint(1,6)
            if(self.sequencia == 1):
                self.moverInimigo1 = True
                self.posicaoInimigo = self.posicaoInimigo - self.velocidade
                if(self.posicaoInimigo < (-210)):
                    self.moverInimigo1 = False
                    self.posicaoInimigo = 801
                imagemInimigo1.move(self.posicaoInimigo, 242)
            elif(self.sequencia == 2):
                self.moverInimigo2 = True
                self.posicaoInimigo = self.posicaoInimigo - self.velocidade
                if(self.posicaoInimigo < (-210)):
                    self.moverInimigo2 = False
                    self.posicaoInimigo = 801
                imagemInimigo2.move(self.posicaoInimigo, 367)
            elif(self.sequencia == 3):
                self.moverInimigo3 = True
                self.posicaoInimigo = self.posicaoInimigo - self.velocidade
                if(self.posicaoInimigo < (-210)):
                    self.moverInimigo3 = False
                    self.posicaoInimigo = 801
                imagemInimigo3.move(self.posicaoInimigo, 493)
            elif(self.sequencia == 4):
                self.moverInimigo1 = True
                self.moverInimigo2 = True
                self.posicaoInimigo = self.posicaoInimigo - self.velocidade
                if(self.posicaoInimigo < (-210)):
                    self.moverInimigo1 = False
                    self.moverInimigo2 = False
                    self.posicaoInimigo = 801
                imagemInimigo1.move(self.posicaoInimigo, 242)
                imagemInimigo2.move(self.posicaoInimigo, 367)
            elif(self.sequencia == 5):
                self.moverInimigo1 = True
                self.moverInimigo3 = True
                self.posicaoInimigo = self.posicaoInimigo - self.velocidade
                if(self.posicaoInimigo < (-210)):
                    self.moverInimigo1 = False
                    self.moverInimigo3 = False
                    self.posicaoInimigo = 801
                imagemInimigo1.move(self.posicaoInimigo, 242)
                imagemInimigo3.move(self.posicaoInimigo, 493)
            elif(self.sequencia == 6):
                self.moverInimigo2 = True
                self.moverInimigo3 = True
                self.posicaoInimigo = self.posicaoInimigo - self.velocidade
                if(self.posicaoInimigo < (-210)):
                    self.moverInimigo2 = False
                    self.moverInimigo3 = False
                    self.posicaoInimigo = 801
                imagemInimigo2.move(self.posicaoInimigo, 367)
                imagemInimigo3.move(self.posicaoInimigo, 493)
            if(checarGameOver() == True):
                timer.stop()
            if(self.contagemPassos < 10):
                self.contagemPassos = self.contagemPassos + 1
            else:
                self.velocidade = self.velocidade + 1
                self.contagemPassos = 0

        timer = QTimer(self)
        timer.timeout.connect(movimentar)
        timer.setInterval(50)
        timer.start()
        self.show()

    #mudar posicao do carro
    def mudarPosicaoYCarro(self, direcao):
        if (direcao == "cima"):
            if(self.enderecoYCarro == 367 or self.enderecoYCarro == 493): 
                if(self.enderecoYCarro == 367): self.enderecoYCarro = 242
                elif(self.enderecoYCarro == 493): self.enderecoYCarro = 367
                imagemCarro.move(6,self.enderecoYCarro)
        elif(direcao == "baixo"):
            if(self.enderecoYCarro == 242 or self.enderecoYCarro == 367): 
                if(self.enderecoYCarro == 242): self.enderecoYCarro = 367
                elif(self.enderecoYCarro == 367): self.enderecoYCarro = 493
                imagemCarro.move(6,self.enderecoYCarro)

    #adicionar ações às teclas
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.mudarPosicaoYCarro("cima")   
        elif event.key() == Qt.Key_Down:
            self.mudarPosicaoYCarro("baixo")   