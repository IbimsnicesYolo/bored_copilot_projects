"""
Generate Tic Tac Toe Game using pygame
"""
import pygame
class TicTacToe:
    """
    Tic Tac Toe Game
    """
    def __init__(self):
        """
        Initialize the game
        """
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.turn = 1
        self.winner = 0
        self.game_over_f = pygame.font.SysFont("comicsans", 60)
        self.game_over_text = self.game_over_f.render("Game Over", True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (300, 300)
        self.reset_game()

    def reset_game(self):
        """
        Reset the game
        """
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.turn = 1
        self.winner = 0

    def check_for_winner(self):
        """
        Check for winner
        """
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            self.winner = self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            self.winner = self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            self.winner = self.board[2][0]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            self.winner = self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            self.winner = self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            self.winner = self.board[0][2]
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
        elif self.turn == 10:
            self.winner = 0
    
    def draw_board(self):
        """
        Draw the board
        """
        self.screen.fill((0, 0, 0))
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 1:
                    pygame.draw.circle(self.screen, (255, 0, 0), (100 + (200 * x), 100 + (200 * y)), 100)
                elif self.board[x][y] == 2:
                    pygame.draw.circle(self.screen, (0, 0, 255), (100 + (200 * x), 100 + (200 * y)), 100)
        pygame.display.update()
    
    def draw_game_over(self):
        """
        Draw the game over screen
        """
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_over_text, self.game_over_rect)
        pygame.display.update()

    def run(self):
        """
        Run the game
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.winner == 0:
                        if pos[0] < 200 and pos[1] < 200 and self.board[0][0] == 0:
                            self.board[0][0] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] < 200 and pos[1] > 200 and pos[1] < 400 and self.board[0][1] == 0:
                            self.board[0][1] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] < 200 and pos[1] > 400 and self.board[0][2] == 0:
                            self.board[0][2] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] > 200 and pos[0] < 400 and pos[1] < 200 and self.board[1][0] == 0:
                            self.board[1][0] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] > 200 and pos[0] < 400 and pos[1] > 200 and pos[1] < 400 and self.board[1][1] == 0:
                            self.board[1][1] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] > 200 and pos[0] < 400 and pos[1] > 400 and self.board[1][2] == 0:
                            self.board[1][2] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] > 400 and pos[1] < 200 and self.board[2][0] == 0:
                            self.board[2][0] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] > 400 and pos[1] > 200 and pos[1] < 400 and self.board[2][1] == 0:
                            self.board[2][1] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        elif pos[0] > 400 and pos[1] > 400 and self.board[2][2] == 0:
                            self.board[2][2] = self.turn
                            self.turn = 3 - self.turn
                            self.check_for_winner()
                        else:
                            self.turn = 3 - self.turn
                    else:
                        self.reset_game()
            if self.winner != 0:
                self.draw_game_over()
            else:
                self.draw_board()
            pygame.display.update()
            self.clock.tick(60)


a = TicTacToe()
a.run()
