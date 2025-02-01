import pygame


class Janela:
  def __init__(self, resolucao_da_tela='HD', cor_da_janela='black',  titulo_da_janela='pygame window', fps=60):
    try:
      # Janelas disponíveis
      self.resolutions = {
        'HD': (1280, 720),
        'FHD': (1920, 1080),
        'CUSTOM': (900, 700)
      }
      self.window = pygame.display.set_mode(self.resolutions[resolucao_da_tela])
    
      pygame.display.set_caption(title=titulo_da_janela)

      # Cores padrão
      self.colors = {
        'branco': (255, 255, 255),
        'cinza': (150, 150, 150),
        'preto': (  0,   0,   0),
        'vermelho': (255,   0,   0),
        'verde': (  0, 255,   0),
        'azul': (  0,   0, 255),
        'laranja': (255, 165,   0)
      }

      self.window.fill(self.colors[cor_da_janela])

      # Informações do mouse
      self.mouse_0 = {'x': None, 'y': None, 'left button': None, 'clicked': False}
      self.mouse = ((0, 0), (False, False, False), (False, False, False))

      # Último estado de clique
      self.last_click_status = (False, False, False)

      self.home_menu = True
      self.pause_menu = False
      self.game_difficulty = 0
    except:
      print('Erro ao criar a janela')