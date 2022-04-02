"""
Create Tetris using pygame
"""
import pygame
import random
import time

class Tetris:
    """
    Tetris class
    """
    def __init__(self):
        """
        Initialize the game
        """
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.paused = False
        self.running = True
        self.score = 0
        self.level = 1
        self.lines = 0
        self.font = pygame.font.SysFont("monospace", 25)
        self.game_over_f = pygame.font.SysFont("monospace", 100)
        self.font_big = pygame.font.SysFont("monospace", 125)
        self.tetrominoes = [
            [[0, 0, 0, 0],[1, 1, 1, 0],[0, 1, 0, 0],[0, 0, 0, 0]],
            [[0, 1, 1, 0],[1, 1, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
            [[0, 0, 1, 0],[0, 0, 1, 0],[0, 0, 1, 0],[0, 0, 1, 0]],
            [[1, 0, 0, 0],[1, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
            [[0, 0, 1, 0],[1, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
            [[0, 1, 1, 0],[1, 1, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
            [[1, 1, 0, 0],[0, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        ]
        self.tetromino_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
        self.tetromino_col = random.choice(self.tetromino_colors)
        self.tetromino_pos = [4, 0]
        self.tetromino_index = random.randint(0, len(self.tetrominoes)-1)
        self.tetromino = self.tetrominoes[self.tetromino_index]
        self.next_tetromino_index = random.randint(0, len(self.tetrominoes)-1)
        self.next_tetromino = self.tetrominoes[self.next_tetromino_index]
        self.next_tetromino_col = random.choice(self.tetromino_colors)
        self.board = [[0 for x in range(10)] for y in range(20)]

        self.game_over = False

    def draw_text(self):
        self.draw_score()
        self.draw_level()
        self.draw_lines()

    def move_left(self):
        """
        Move the tetromino left
        """
        self.move_tetromino(-1, 0)

    def move_right(self):
        """
        Move the tetromino left
        """
        self.move_tetromino(1, 0)

    def check_keys(self):
        """
        Check for keys
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left()
                if event.key == pygame.K_RIGHT:
                    self.move_right()
                if event.key == pygame.K_DOWN:
                    self.drop_tetromino()
                if event.key == pygame.K_UP:
                    self.rotate_tetromino()
                if event.key==pygame.K_TAB:
                    self.paused = not self.paused

    def run(self):
        """
        Run the game
        """
        tick = 0
        while self.running:
            self.clock.tick(20)
            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.draw_next_tetromino()
            self.draw_text()
            self.check_for_collision()
            if not self.paused:
                if tick % 5 == 0:
                    self.drop_tetromino()
                self.check_for_collision()
                self.check_over()
            else:
                self.draw_paused()
            self.draw_tetromino()
            self.check_keys()
            pygame.display.update()
            pygame.display.flip()

            tick = tick + 1
            if tick > 1000:
                tick = 1


    def draw_board(self):
        """
        Draw the board
        """
        for x in range(10):
            for y in range(20):
                if self.board[y][x] != 0:
                    pygame.draw.rect(self.screen, self.board[y][x], (x * 30 , y * 30, 30, 30), 0)
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x * 30, y * 30, 30, 30), 1)

    def draw_next_tetromino(self):
        """
        Draw the next tetromino
        """
        for x in range(4):
            for y in range(4):
                if self.next_tetromino[y][x] != 0:
                    pygame.draw.rect(self.screen, self.next_tetromino_col, (x * 30 + 400, y * 30 + 100, 30, 30), 0)

        score_text = self.font.render("Next:", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.center = (430, 50)
        self.screen.blit(score_text, score_rect)

    def draw_paused(self):
        """
        Draw the paused text
        """
        paused_text = self.font_big.render("Paused", True, (255, 255, 255))
        paused_rect = paused_text.get_rect()
        paused_rect.center = (300, 300)
        self.screen.blit(paused_text, paused_rect)

    def draw_score(self):
        """
        Draw the score
        """
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.center = (400, 250)
        self.screen.blit(score_text, score_rect)

    def draw_level(self):
        """
        Draw the level
        """
        level_text = self.font.render("Level: " + str(self.level), True, (255, 255, 255))
        level_rect = level_text.get_rect()
        level_rect.center = (400, 300)
        self.screen.blit(level_text, level_rect)

    def draw_lines(self):
        """
        Draw the lines
        """
        lines_text = self.font.render("Lines: " + str(self.lines), True, (255, 255, 255))
        lines_rect = lines_text.get_rect()
        lines_rect.center = (400, 350)
        self.screen.blit(lines_text, lines_rect)

    def draw_tetromino(self):
        """
        Draw the tetromino
        """
        for x in range(4):
            for y in range(4):
                if self.tetromino[y][x] != 0:
                    pygame.draw.rect(self.screen, self.tetromino_col, (x * 30 + self.tetromino_pos[0] * 30, y * 30 + self.tetromino_pos[1] * 30, 30, 30), 0)

    def check_for_collision(self):
        """
        Check for collision
        """
        for x in range(4):
            for y in range(4):
                if self.tetromino[y][x] != 0:
                    if len(self.board) <= self.tetromino_pos[1] + y:
                        self.stop_tetromino()
                    if self.board[self.tetromino_pos[1] + y][self.tetromino_pos[0] + x] != 0:
                        if self.tetromino_pos[1] + y < 2:
                            self.game_over = True
                        else:
                            self.stop_tetromino()

    def check_for_collision_next(self):
        self.tetromino_pos[1] += 1
        self.check_for_collision()
        self.tetromino_pos[1] -= 1

    def check_wall_collision(self):
        """
        Check for collision
        """
        for x in range(4):
            for y in range(4):
                if self.tetromino[y][x] != 0:
                    if self.tetromino_pos[0] + x < 0:
                        self.move_tetromino(1, 0)
                    if self.tetromino_pos[0] + x > 9:
                        self.move_tetromino(-1, 0)

    def stop_tetromino(self):
        for x in range(4):
            for y in range(4):
                if self.tetromino[y][x] != 0:
                    self.board[self.tetromino_pos[1] + y - 1][self.tetromino_pos[0] + x] = self.tetromino_col
        self.update_tetromino()
        self.check_for_line()

    def update_tetromino(self):
        self.tetromino_index = self.next_tetromino_index
        self.tetromino = self.next_tetromino
        self.tetromino_pos = [4, 0]
        self.tetromino_col = self.next_tetromino_col

        self.next_tetromino_col = random.choice(self.tetromino_colors)
        self.next_tetromino_index = random.randint(0, len(self.tetrominoes)-1)
        self.next_tetromino = self.tetrominoes[self.next_tetromino_index]

    def check_over(self):
        """
        Check for game over
        """
        if self.game_over:
            self.check_for_game_over_text()
            self.screen.blit(self.game_over_text, self.game_over_rect)
            pygame.display.flip()
            time.sleep(5)
            self.running = False

    def move_tetromino(self, x, y):
        """
        Move the tetromino
        """
        self.tetromino_pos[0] += x
        self.tetromino_pos[1] += y

        self.check_wall_collision()

    def rotate_tetromino(self):
        """
        Rotate the tetromino
        """
        self.tetromino = list(zip(*self.tetromino[::-1]))
        self.check_wall_collision()
    
    def drop_tetromino(self):
        """
        Drop the tetromino
        """
        self.check_for_collision_next()
        self.tetromino_pos[1] += 1

    def check_for_line(self):
        """
        Check for line
        """
        combo = 0
        for y in range(20):
            if 0 not in self.board[y]:
                self.board.pop(y)
                self.board.insert(0, [0 for x in range(10)])
                combo += 1

        self.lines += combo
        self.score += 10 * (combo*combo)
        self.level = self.lines // 10 + 1
    
    def check_for_level(self):
        """
        Check for level
        """
        if self.lines % 10 == 0:
            self.level += 1
            self.score += 10

    def check_for_game_over_text(self):
        """
        Check for game over text
        """
        self.game_over_text = self.game_over_f.render("Game Over", True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (300, 300)

game = Tetris()
game.run()
