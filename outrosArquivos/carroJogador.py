class Carro:
    spriteAtual = "\\imagens\\carro1.png"
    velocidade = 1

    def mudarSprite(self):
        if(self.spriteAtual == "\\imagens\\carro1.png"): self.spriteAtual = "\\imagens\\carro2.png"
        else: self.spriteAtual = "\\imagens\\carro1.png"
        return self.spriteAtual
    
    def aumentarVelocidade(self):
        self.velocidade = self.velocidade + 1