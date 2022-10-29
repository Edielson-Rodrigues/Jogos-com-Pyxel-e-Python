import pyxel
import random 

#criando classe Snake(cobra)
class Snake:
    def __init__(self, x, y):
        self.posicaoAtual = [x, y]
        self.CIMA = -8
        self.BAIXO = 8
        self.ESQUERDA = -8
        self.DIREITA = 8
        self.direcaoX = self.DIREITA
        self.direcaoY = 0
        self.desenho = [0, 0, 8, 8]
        
#criando classe Game(Jogo)
class Game:
    def __init__(self):
        pyxel.init(144, 144, title='Snake', fps=60)
        self.cobra = Snake(8, 8)
        pyxel.load('snake.pyxres') #lendo banco de imagens
        self.condicaoMudarMovimento = True
        self.condicaoPosicaoComida = True
        self.contadorPlacar = 0
        self.placarAtualDigito1, self.placarAtualDigito2 = self.adcionarPontuancao()
        self.condicaoAdicionarCobra = False
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.condicaoMudarMovimento:
            #aplicando mudança de direção no eixo X
            if pyxel.btn(pyxel.KEY_RIGHT) and self.cobra.direcaoX != self.cobra.ESQUERDA or pyxel.btn(pyxel.KEY_D) and self.cobra.direcaoX != self.cobra.ESQUERDA:
                self.cobra.direcaoX = self.cobra.DIREITA
                self.cobra.direcaoY = 0
                self.cobra.desenho = (0, 0, 8, 8)

            elif pyxel.btn(pyxel.KEY_LEFT) and self.cobra.direcaoX != self.cobra.DIREITA or pyxel.btn(pyxel.KEY_A) and self.cobra.direcaoX != self.cobra.DIREITA:
                self.cobra.direcaoX = self.cobra.ESQUERDA
                self.cobra.direcaoY = 0
                self.cobra.desenho = (8, 8, 8, 8)

                #aplicando mudança de direção no eixo Y
            elif pyxel.btn(pyxel.KEY_UP) and self.cobra.direcaoY != self.cobra.BAIXO or pyxel.btn(pyxel.KEY_W) and self.cobra.direcaoY != self.cobra.BAIXO:
                self.cobra.direcaoY = self.cobra.CIMA
                self.cobra.direcaoX = 0
                self.cobra.desenho = (8, 0, 8, 8)

            elif pyxel.btn(pyxel.KEY_DOWN) and self.cobra.direcaoY != self.cobra.CIMA or pyxel.btn(pyxel.KEY_S) and self.cobra.direcaoY != self.cobra.CIMA:
                self.cobra.direcaoY = self.cobra.BAIXO
                self.cobra.direcaoX = 0
                self.cobra.desenho = (0, 8, 8, 8)

            self.condicaoMudarMovimento = False

        else:
            if self.cobra.posicaoAtual[0] <= pyxel.width-8 and self.cobra.posicaoAtual[0] >= 0 and self.cobra.posicaoAtual[1] >= 0 and self.cobra.posicaoAtual[1] <= pyxel.height-8:
                self.condicaoMudarMovimento = True

        if pyxel.frame_count % 15 == 0:
            #movimentando cobra
            self.cobra.posicaoAtual[0] += self.cobra.direcaoX
            self.cobra.posicaoAtual[1] += self.cobra.direcaoY

            #realocando posição quando ela passar dos limites do eixo x
            if self.cobra.direcaoX == self.cobra.DIREITA:
                if self.cobra.posicaoAtual[0] > pyxel.width:
                    self.cobra.posicaoAtual[0] = -8
                    
            elif self.cobra.direcaoX == self.cobra.ESQUERDA:
                if self.cobra.posicaoAtual[0] <= -8:
                    self.cobra.posicaoAtual[0] = pyxel.width + 8

            #realocando posição quando ela passar dos limites do eixo y
            elif self.cobra.direcaoY == self.cobra.BAIXO:
                if self.cobra.posicaoAtual[1] > pyxel.height:
                    self.cobra.posicaoAtual[1] = -8
            
            elif self.cobra.direcaoY == self.cobra.CIMA:
                if self.cobra.posicaoAtual[1] <= -8:
                    self.cobra.posicaoAtual[1] = pyxel.height + 8

        #pegando valores sorteados para as coordenadas da comida
        if self.condicaoPosicaoComida:
            self.localSorteadoX, self.localSorteadoY = self.comida()
            self.condicaoPosicaoComida = False
        
        elif self.cobra.posicaoAtual[0] == self.localSorteadoX and self.cobra.posicaoAtual[1] == self.localSorteadoY:
            self.condicaoPosicaoComida = True
            self.contadorPlacar += 1
            self.placarAtualDigito1, self.placarAtualDigito2 = self.adcionarPontuancao()
            #self.condicaoAdicionarCobra = True
    
    def draw(self):
        #desenhando na tela
        pyxel.cls(11)
        pyxel.blt(self.cobra.posicaoAtual[0], self.cobra.posicaoAtual[1], 0, self.cobra.desenho[0], self.cobra.desenho[1], self.cobra.desenho[2], self.cobra.desenho[3], 14) #desenhando a cobra 
        pyxel.blt(self.localSorteadoX, self.localSorteadoY, 0, 16, 8, 16, 8, 14) #desenhando a comida
        pyxel.blt(pyxel.width-14, 1, 1, self.placarAtualDigito1[0], self.placarAtualDigito1[1], self.placarAtualDigito1[2], self.placarAtualDigito1[3], 10) #desenhando primeiro digito do placar
        pyxel.blt(pyxel.width-8, 1, 1, self.placarAtualDigito2[0], self.placarAtualDigito2[1], self.placarAtualDigito2[2], self.placarAtualDigito2[3], 10) #desenhando segundo digito do placar
        
    #criando função para gerar posições aleátorias para comida
    def comida(self):
        auxiliar1 = 0
        auxiliar2 = 0
        posicoesDisponiveisHorizontal = []
        posicoesDisponiveisVertical = []
        sorteioX = None
        sorteioY = None

        #verificando se a largura é igual a altura
        if pyxel.width == pyxel.height:
            #sorteando posições a cada 8 pixels
            while auxiliar1 <= pyxel.width:
                if auxiliar1 % 8 == 0:
                    posicoesDisponiveisHorizontal.append(auxiliar1)
                    posicoesDisponiveisVertical.append(auxiliar1)
                auxiliar1 += 1
            
            #sorteando posições para x e y baseado nas posições disponíveis
            sorteioX = random.randrange(0, len(posicoesDisponiveisHorizontal)-1)
            sorteioY = random.randrange(0, len(posicoesDisponiveisVertical)-1)

        #caso largura e altura sejam diferentes...
        else: 
            #sorteando posições acada 8 pixels
            while auxiliar1 <= pyxel.width:
                if auxiliar1 % 8 == 0:
                    posicoesDisponiveisHorizontal.append(auxiliar1)
                auxiliar1 += 1
            
            while auxiliar2 <= pyxel.height:
                if auxiliar2 % 8 == 0:
                    posicoesDisponiveisVertical.append(auxiliar2)
                auxiliar2 += 1
            
            #sorteando posições para x e y baseado nas posições disponíveis
            sorteioX = random.randrange(0, len(posicoesDisponiveisHorizontal)-1)
            sorteioY = random.randrange(0, len(posicoesDisponiveisVertical)-1)

        #atribuindo valores para retorna no update
        posicaoSorteadaX = posicoesDisponiveisHorizontal[sorteioX]
        posicaoSorteadaY = posicoesDisponiveisVertical[sorteioY]
            
        return posicaoSorteadaX, posicaoSorteadaY        
    
    #Função para contabilizar 
    def adcionarPontuancao(self):
        #posições do bando de imagem de acordo com o placar
        posicoes = [(0, 0, 8, 8), (8, 0, 8, 8), (0, 8, 8, 8), (8, 8, 8, 8), (16, 0, 8, 8), (16, 8, 8, 8), (24, 0, 8, 8), (24, 8, 8, 8), (32, 0, 8, 8), (32, 8, 8, 8)]
        
        primeiroDigito = None
        segundoDigito = None
        #Verificando se o placar é menor que 9
        if self.contadorPlacar <= 9:
            primeiroDigito = posicoes[0]
            segundoDigito = posicoes[self.contadorPlacar]
        #Verificando se o placar é maior que 9
        elif self.contadorPlacar > 9:
            transforma = str(self.contadorPlacar)
            primeiroDigito = posicoes[int(transforma[0])]
            segundoDigito = posicoes[int(transforma[1])]
            
        return primeiroDigito, segundoDigito

    def adicionarCobra(self):
        pass
Game()