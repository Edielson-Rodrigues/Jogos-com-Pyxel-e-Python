import pyxel
from nave import Nave #importano do arquivo nave a class Nave

class Game:
    def __init__(self):
        pyxel.init(112, 112, title='Game')
        pyxel.load('image_bank.pyxres') #lendo banco de imagens
        self.nave = Nave() #criando instância
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.nave.movimentandoNave()       

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.nave.posicaoX, pyxel.height-24, 0, self.nave.desenhoNave[0], self.nave.desenhoNave[1], self.nave.desenhoNave[2], self.nave.desenhoNave[3], 7)
        self.nave.tirosNave()
Game()