import pygame

class JogoDaVelha:
  offset: int = 50
  COLORS: dict = {
    'branco': (255, 255, 255),
    'cinza': (150, 150, 150),
    'preto': (0, 0, 0),
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'laranja': (255, 165, 0),
    'azul claro': (200, 200, 255)
  }
  rows: int = 0
  cols: int = 0
  size: int = 0
  end_game: bool = False
  turn: str = ''
  score: list = []
  count_end_game: int = 0
  font: pygame.font.Font

  def __init__(self):
    pygame.font.init()
    self.font = pygame.font.SysFont("Courier New", 50, bold=True)

    self.tabuleiro_map = [
      ['', '', ''],
      ['', '', ''],
      ['', '', '']
    ]
    self.turn = 'x'
    self.score = [0, 0]
    self.end_game = False
    self.count_end_game = 0


  def tabuleiro(self, window, matriz, cor='preto'):
    if self.verifica_matriz(matriz):
      if self.size == 3:
        pygame.draw.line(window, self.COLORS[cor], (self.offset + 200, self.offset), (self.offset + 200, self.offset + 600), 9)
        pygame.draw.line(window, self.COLORS[cor], (self.offset + 400, self.offset), (self.offset + 400, self.offset + 600), 9)
        pygame.draw.line(window, self.COLORS[cor], (self.offset, self.offset + 200), (self.offset + 600, self.offset + 200), 9)
        pygame.draw.line(window, self.COLORS[cor], (self.offset, self.offset + 400), (self.offset + 600, self.offset + 400), 9)
      else:
        self.tabuleiro_didatico(window, cor)
    else:
      print('Matriz inválida')


  def tabuleiro_didatico(self, window, cor):
    cell_size = 500 // max(self.rows, self.cols)

    # Desenha as linhas verticais
    for i in range(1, self.size):
      x = self.offset + i * cell_size
      pygame.draw.line(window, self.COLORS[cor], (x, self.offset), (x, self.offset + self.size * cell_size), 9)

    # Desenha as linhas horizontais
    for i in range(1, self.size):
      y = self.offset + i * cell_size
      pygame.draw.line(window, self.COLORS[cor], (self.offset, y), (self.offset + self.size * cell_size, y), 9)

    # Desenha os números das posições
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 25, bold=True)
    for row in range(self.rows):
      for col in range(self.cols):
        x = self.offset + col * cell_size + cell_size // 2 - 17  # Ajuste de posição
        y = self.offset + row * cell_size + cell_size // 2 - 2 # Ajuste de posição
        text = font.render(f"({row+1},{col+1})", True, self.COLORS['azul'])  # Texto da posição
        window.blit(text, (x, y))  # Desenha o texto na tela

    # Desenha a borda do tabuleiro
    board_width = self.cols * cell_size
    board_height = self.rows * cell_size
    pygame.draw.rect(window, self.COLORS[cor], (self.offset - 5, self.offset - 5, board_width + 10, board_height + 10), 9)

    # Exibe o tamanho da matriz abaixo do tabuleiro
    text = font.render(f"{self.rows}x{self.cols}", True, self.COLORS['azul'])
    text_rect = text.get_rect(center=(self.offset + (self.cols * cell_size) // 2, self.offset + self.rows * cell_size + 30))
    window.blit(text, text_rect)


  def verifica_matriz(self, matriz) -> bool:
    if not isinstance(matriz, list):
      return False

    self.size = len(matriz)
    self.rows = self.size
    self.cols = self.size

    if self.size == 0:
      return True

    for l in matriz:
      if not isinstance(l, list):
        return False
      if len(l) != self.size:
        return False

    return True


  def __tabuleiro_hover(self, window, mouse):
    for y in range(3):
      for x in range(3):
        if mouse[0][0] >= self.offset + (x * 200) and mouse[0][0] < self.offset + (x * 200) + 200 and \
          mouse[0][1] >= self.offset + (y * 200) and mouse[0][1] < self.offset + (y * 200) + 200:
          pygame.draw.rect(window, self.COLORS['azul claro'], (self.offset + (x * 200), self.offset + (y * 200), 200, 200))


  def evento_de_clique(self, janela) -> None:
    self.__tabuleiro_hover(janela.configuracao, janela.mouse)
    mouse = janela.mouse
    for y in range(3):
      for x in range(3):
        if mouse[0][0] >= self.offset + (x * 200) and mouse[0][0] < self.offset + (x * 200) + 200 and \
          mouse[0][1] >= self.offset + (y * 200) and mouse[0][1] < self.offset + (y * 200) + 200:
          if mouse[2][0] == True and self.tabuleiro_map[y][x] == '' and self.end_game == False:
            self.tabuleiro_map[y][x] = self.turn
            self.turn = 'o' if self.turn == 'x' else 'x'

  def desenha_x_e_o(self, janela, cor_do_x, cor_do_o):
    for y in range(3):
      for x in range(3):
        if self.tabuleiro_map[y][x] == 'x':
          pygame.draw.line(janela.configuracao, self.COLORS[cor_do_x], (self.offset + (x * 200) + 50, self.offset + (y * 200) + 50), \
                                                  (self.offset + (x * 200) + 150, self.offset + (y * 200) + 150), 16)
          pygame.draw.line(janela.configuracao, self.COLORS[cor_do_x], (self.offset + (x * 200) + 150, self.offset + (y * 200) + 50), \
                                                  (self.offset + (x * 200) + 50, self.offset + (y * 200) + 150), 16)
        elif self.tabuleiro_map[y][x] == 'o':
          pygame.draw.circle(janela.configuracao, self.COLORS[cor_do_o], (self.offset + (x * 200) + 100, self.offset + (y * 200) + 100), 50, 16)

