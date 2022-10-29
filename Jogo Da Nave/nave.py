import pyxel

class Nave:
    def __init__(self): 
        self.desenhoNave = (0, 0, 8, 8) #Posição do desenho no banco de imagens
        self.desenhoTiros = (11, 3, 12, 6)
        self.posicaoX = 0
        self.posicaoYtiros = 30
    def movimentandoNave(self):
        #Incrementando movimento da nave
        if self.posicaoX < pyxel.width-8:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.posicaoX += 1
        if self.posicaoX > 0:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.posicaoX -= 1
    

    def tirosNave(self):
        #Criando animações dos tiros
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pass
            # while self.posicaoYtiros > 0:
            #     pyxel.blt(self.posicaoX, pyxel.height-self.posicaoYtiros, 0, self.desenhoTiros[0], self.desenhoTiros[1], self.desenhoTiros[2], self.desenhoTiros[3], 7)
            #     pyxel.blt(self.posicaoX+7, pyxel.height-self.posicaoYtiros, 0, self.desenhoTiros[0], self.desenhoTiros[1], self.desenhoTiros[2], self.desenhoTiros[3], 7)
            #     self.posicaoYtiros += 1
        """
        Achar um jeito de movimentar as balas até sumirem da tela, mesmo com o botão não pressionado
        """    
Nave()  