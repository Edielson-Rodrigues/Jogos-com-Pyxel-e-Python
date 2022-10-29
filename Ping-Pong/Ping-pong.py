import random
import pyxel

class ping_pong:

    def __init__(self):
        #criando variáveis 
        pyxel.init(160, 100, title="Ping-Pong", fps=60)
        self.ALTURA = 14
        self.LARGURA = 2
        self.RAIO = 1.5
        self.VELOCIDADE_BOLINHA = 1
        self.X_BOTAO_ESQUERDO = 2
        self.yBotaoEsquerdo = (pyxel.height/2) - 8
        self.X_BOTAO_DIREITO = pyxel.width - 4
        self.yBotaoDireito = (pyxel.height/2) - 8
        self.posicaoBolinha = [(pyxel.width/2)-1, pyxel.height/2]
        self.condicaoBolinhaX = True
        self.condicaoBolinhaY = True
        self.placarJ1 = 0
        self.placarJ2 = 0
        self.resultado = ""
        self.CondicaoRecomecarJogo = True
        pyxel.run(self.update, self.draw)
    
    
    def update(self):
        
        #verificando se a partida ainda não acabou
        if self.placarJ1 < 7 and self.placarJ2 < 7 and self.CondicaoRecomecarJogo:

        #movimentando botões
            if pyxel.btn(pyxel.KEY_W) and self.yBotaoEsquerdo != 1:
                self.yBotaoEsquerdo = (self.yBotaoEsquerdo - 1)
            if pyxel.btn(pyxel.KEY_S) and self.yBotaoEsquerdo != pyxel.height - (self.ALTURA + 1):
                self.yBotaoEsquerdo = (self.yBotaoEsquerdo + 1)
            if pyxel.btn(pyxel.KEY_UP) and self.yBotaoDireito != 1:
                self.yBotaoDireito = (self.yBotaoDireito - 1)
            if pyxel.btn(pyxel.KEY_DOWN) and self.yBotaoDireito != pyxel.height - (self.ALTURA + 1):
                self.yBotaoDireito = (self.yBotaoDireito + 1)

        #movimento bolinha
            checarCadaPyxelDaAltura = -4
            
            if self.condicaoBolinhaX:
                self.posicaoBolinha[0] += self.VELOCIDADE_BOLINHA
                #checando colisão com plataforma da direita
                while checarCadaPyxelDaAltura <= self.ALTURA :
                    checarCadaPyxelDaAltura += 1
                    if (self.posicaoBolinha[0] + (self.RAIO * 2) == self.X_BOTAO_DIREITO and self.posicaoBolinha[1] == self.yBotaoDireito + checarCadaPyxelDaAltura):
                        self.condicaoBolinhaX = False
                    #checando se a bola passou e atualizando placar 
                    if self.posicaoBolinha[0] > pyxel.width:
                        self.placarJ1 += 1
                        #Realocando a bola em um lugar aleatório do eixo y
                        self.posicaoBolinha = [(pyxel.width/2)-1, random.randrange(self.RAIO * 2, (pyxel.height - (self.RAIO * 2)))]
                        self.condicaoBolinhaX = False
            else:   
                self.posicaoBolinha[0] -= self.VELOCIDADE_BOLINHA
                #checando colisão com plataforma da esquerda
                while checarCadaPyxelDaAltura <= self.ALTURA:
                    checarCadaPyxelDaAltura += 1
                    if self.posicaoBolinha[0] + (self.RAIO * 2) == (self.X_BOTAO_ESQUERDO + (self.LARGURA + 5)) and self.posicaoBolinha[1] == self.yBotaoEsquerdo + checarCadaPyxelDaAltura:
                        self.condicaoBolinhaX = True
                    #checando se a bola passou e atualizando placar 
                    if self.posicaoBolinha[0] < 0:
                        self.placarJ2 += 1
                        #Realocando a bola em um lugar aleatório do eixo y
                        self.posicaoBolinha = [(pyxel.width/2)-1, random.randrange(self.RAIO * 2, (pyxel.height - (self.RAIO *2)))]
                        self.condicaoBolinhaX = True
                                

            if self.condicaoBolinhaY:
                self.posicaoBolinha[1] += self.VELOCIDADE_BOLINHA
                #checando colisão com borda inferior
                if self.posicaoBolinha[1] + (self.RAIO * 2) + 1 == pyxel.height: 
                    self.condicaoBolinhaY = False
                
            else:
                self.posicaoBolinha[1] -= self.VELOCIDADE_BOLINHA
                #checando colisão com borda superior
                if self.posicaoBolinha[1] - 3 == 0:
                    self.condicaoBolinhaY = True
        
        
        else:
            #parando jogo
            self.CondicaoRecomecarJogo = False
            if self.CondicaoRecomecarJogo == False:
                #atribuindo valor ao self.resultado, para o exibir na tela
                if self.placarJ1 == 7:
                    self.resultado = "Jogador Um, Wins!!!"
                
                if self.placarJ2 == 7:
                    self.resultado = "Jogador Dois, Wins!!!"
            #recomeçando jogo
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.placarJ1 = 0
                self.placarJ2 = 0
                self.resultado = ''
                self.yBotaoDireito = (pyxel.height/2) - 8
                self.yBotaoEsquerdo = (pyxel.height/2) - 8
                self.posicaoBolinha = [(pyxel.width/2)-1, pyxel.height/2]
                self.CondicaoRecomecarJogo = True

    def draw(self):
        #desenhando na tela
        pyxel.cls(0)
        pyxel.rect(self.X_BOTAO_ESQUERDO, self.yBotaoEsquerdo, self.LARGURA, self.ALTURA, 7)
        pyxel.rect(self.X_BOTAO_DIREITO, self.yBotaoDireito, self.LARGURA, self.ALTURA, 7)
        pyxel.line((pyxel.width/2) - 1, 0, (pyxel.width/2) - 1, pyxel.height, 6)
        pyxel.circ(self.posicaoBolinha[0], self.posicaoBolinha[1], self.RAIO, 9)
        pyxel.text((pyxel.width / 2) - 20, 3, str(self.placarJ1), 7)
        pyxel.text((pyxel.width / 2) + 15, 3, str(self.placarJ2), 7)
        pyxel.text((pyxel.width / 2) - (pyxel.width / 4), (pyxel.height / 2), self.resultado, 7)
        pyxel.rectb(0, 0, pyxel.width, pyxel.height, 8)

ping_pong()