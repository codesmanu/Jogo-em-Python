import pygame 
import os 
import random 

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transforme.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transforme.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transforme.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transforme.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
    pygame.transforme.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png')))
    pygame.transforme.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
    ]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont ("arial", 50)
 
class Passaro:
   IMGS = IMAGENS_PASSARO
   #animações de rotação
   ROTAÇÃO_MAXIMA = 25
   VELOCIDADE_ROTACAO = 20
   TEMPO_ANIMAÇAO = 5 

   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.angulo = 0 
      self.altura = self.y
      self.tempo = 0 
      self.contagem_imagem = 0 
      self.imagem = IMGS[0]
      
    def pular (self):
         self.velocidade = -10,5
         self.tempo = 0 
         self.altura = self.y 

    def nover(self):
      self.tempo += 1
      deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo 

      # restringir o deslocamento 
      if deslocamento > 16; 
         deslocamento = 16

      elif deslocamento < 0;
         deslocamento -= 2

      self.y += deslocamento

      # o angulo do passaro 
      if deslocamento < 0 or self.y < (self.altura + 50)
       if self.angulo < self.ROTAÇÃO_MAXIMA
        self.angulo = self.ROTAÇÃO_MAXIMA

    else:
    if self.angulo > -90:
           self.angulo -= self.VELOCIDADE_ROTAÇAO

        
    def desenhar(self, tela):
      #definir qual imagem do passaro vai usar 
      self.contagem_imagem += 1

      if self.contagem_imagem < self.TEMPO_ANIMAÇAO:
         self.imagem = self. IMGS[0]
      elif self.contagem_imagem < self.TEMPO_ANIMAÇAO*2:
        self.imagem = self.IMGS[1]
      elif self.contagem_imagem < self.TEMPO_ANIMAÇAO*3:
         self.imagem = self.IMGS[2]
      elif self.contagem_imagem < self.TEMPO_ANIMAÇAO*4:
         self.imagem = self.IMGS[1]
      elif self.contagem_imagem >= self.TEMPO_ANIMAÇAO*4 + 1:
          self.imagem = self.IMGS[0]
          self.contagem_imagem = 0 

    #se o passaro tiver caindo, eu não vou bater asa 
       if self.angulo <= -80: 
         self.imagem = self.IMGS[1]
         self.contagem_imagem = self.TEMPO_ANIMAÇAO*2

         #desenhar a imagem 
         imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
         pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
         retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
         tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
      pygame.mask.from_surface(self.imagem)






class Cano:
    pass

class Chao:
 pass 